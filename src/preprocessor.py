import logging
import json
from typing import Dict, List, Optional

from channel import Channel
from channel_member import ChannelMember
from channel_member_history_entry import ChannelMemberHistoryEntry
from team_member import TeamMember
from team import Team


class Preprocessor:
    contents: Optional[str]

    channels: List[Channel]
    channel_members: List[ChannelMember]
    channel_member_histories: List[ChannelMemberHistoryEntry]
    team_members: List[TeamMember]
    teams: List[Team]

    def __init__(self, data_file_path: str):
        with open(data_file_path) as f:
            self.contents = json.load(f)
        self.channels = []
        self.channel_members = []
        self.channel_member_histories = []
        self.team_members = []
        self.teams = []

    def load_all(self) -> None:
        """
        Load everything from the content file into their variables,
        then free the content memory.
        """
        self.load_channels()
        self.load_channel_members()
        self.load_channel_member_histories()
        self.load_team_members()

        self.add_channel_member_history_to_channels()

        self.find_team_channels_and_members()

        self.free_content()

    def load_channels(self) -> None:
        """
        Load every channel from json file.
        """
        channels = self.contents["channels"]

        for channel in channels:
            self.channels.append(Channel(
                channel_id=channel["ChannelId"],
                team_id=channel["TeamId"],
                creator_id=channel["CreatorId"],
                create_at=channel["CreateAt"],
                delete_at=channel["DeleteAt"],
                total_msg_count=channel["TotalMsgCount"],
                post_count=channel["PostCount"],
                reactions_count=channel["ReactionsCount"],
                channel_members=[],
                channel_member_history=[]
            ))

    def load_channel_members(self) -> None:
        """
        Load every channel member from json file.
        """
        channel_members = self.contents["channel_members"]

        for channel_member in channel_members:
            self.channel_members.append(ChannelMember(
                channel_id=channel_member["ChannelId"],
                user_id=channel_member["UserId"],
                msg_count=channel_member["MsgCount"],
                mention_count=channel_member["MentionCount"]
            ))

    def load_channel_member_histories(self) -> None:
        """
        Load every channel member history from json file.
        """
        channel_member_histories = self.contents["channel_member_history"]

        for channel_member_history in channel_member_histories:
            self.channel_member_histories.append(ChannelMemberHistoryEntry(
                channel_id=channel_member_history["ChannelId"],
                user_id=channel_member_history["UserId"],
                join_time=channel_member_history["JoinTime"],
                leave_time=channel_member_history["LeaveTime"]
            ))

    def load_team_members(self) -> None:
        """
        Load every team member from json file.
        """
        team_members = self.contents["team_members"]

        for team_member in team_members:
            self.team_members.append(TeamMember(
                team_id=team_member["TeamId"],
                user_id=team_member["UserId"],
                delete_at=team_member["DeleteAt"]
            ))

    def add_channel_member_history_to_channels(self):
        """
        Add the history of channel members joining/leaving
        to the respective channels.
        """
        # Map from channel_id to list of history entries
        channel_history_map: Dict[str, List[ChannelMemberHistoryEntry]] = {}
        for entry in self.channel_member_histories:
            history_list = channel_history_map.get(entry.channel_id)

            if history_list is None:
                history_list = []

            history_list.append(entry)

            channel_history_map[entry.channel_id] = history_list

        for channel in self.channels:
            channel.channel_member_history = channel_history_map.get(
                channel.channel_id)

    def find_team_channels_and_members(self):
        """
        Find every channel and team member related to each team,
        and add it to the team.
        """
        # Create a dict that maps channel_id to members of it.
        channel_member_map: Dict[str, List[ChannelMember]] = {}
        for channel_member in self.channel_members:
            channel_member_list = channel_member_map.get(
                channel_member.channel_id)

            if channel_member_list is None:
                channel_member_list = []

            channel_member_list.append(channel_member)
            channel_member_map[channel_member.channel_id] = channel_member_list

        # Get all channels that belong to the teams
        team_channels: Dict[str, List[Channel]] = {}
        for channel in self.channels:
            # Add the members to the channel
            channel_members = channel_member_map.get(channel.channel_id)

            # Some channels might not have any users in it
            if channel_members is None:
                channel_members = []

            channel.channel_members = channel_members

            team_channel_list = team_channels.get(channel.team_id)

            if team_channel_list is None:
                team_channel_list = []

            team_channel_list.append(channel)

            team_channels[channel.team_id] = team_channel_list

        # Find all members of each team, and create map of it
        team_members_map: Dict[str, List[TeamMember]] = {}
        for team_member in self.team_members:
            team_member_list = team_members_map.get(team_member.team_id)

            if team_member_list is None:
                team_member_list = []

            team_member_list.append(team_member)

            team_members_map[team_member.team_id] = team_member_list

        # Create all teams
        for (team_id, channels) in team_channels.items():
            self.teams.append(Team(
                team_id=team_id,
                channels=channels,
                team_members=team_members_map.get(team_id)
            ))

    def free_content(self):
        """
        Release the memory of content.
        """
        if self.contents is not None:
            del self.contents
