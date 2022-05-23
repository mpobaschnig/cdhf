# data.py
#
# Copyright 2022 Martin Pobaschnig
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with this program.  If not, see <http: //www.gnu.org/licenses/>.

import json

from typing import Dict, List, Optional, Tuple

from .channel import Channel
from .channel_member import ChannelMember
from .channel_member_history_entry import ChannelMemberHistoryEntry
from .team_member import TeamMember
from .team import Team
from .user_data import UserData


class Data:
    """A class used for processing and holding the data set"""
    file_path: Optional[str]

    __contents: Optional[str]

    channels: List[Channel]
    """List of all channels."""
    channel_members: List[ChannelMember]
    """List of all channel members."""
    channel_member_histories: List[ChannelMemberHistoryEntry]
    """List of every channel member history event."""
    team_members: List[TeamMember]
    """List of every team member."""
    teams: List[Team]
    """List of all teams."""
    users: Dict[str, UserData]
    """Dictionary of all users and their associated user data."""

    building_members: Dict[str, List[int]] = {}
    """Dictionary that maps the building to its members."""
    org_unit_members: Dict[str, List[int]] = {}
    """Dictionary that maps the organisational unit to its members."""

    def __init__(self, data_file_path: str = None):
        """
        Args:
            data_file_path (str, optional): Path to data set file. 
                If none, use default path. Defaults to None.
        """
        self.channels = []
        self.channel_members = []
        self.channel_member_histories = []
        self.team_members = []
        self.teams = []
        self.users = {}

        if data_file_path is None:
            data_file_path = "input/mmdata.json"
        self.file_path = data_file_path

    def load_all(self) -> None:
        """Load everything from the content file."""
        with open(self.file_path) as f:
            self.__contents = json.load(f)

        self.__load_teams()
        self.__load_team_members()
        self.__load_channels()
        self.__load_channel_members()
        self.__load_channel_member_histories()
        self.__load_users()

        self.__add_channel_member_history_to_channels()

        self.__find_team_channels_and_members()

        self.__find_building_and_org_unit_members()

        self.__add_remaining_users_user_data()

    def __load_channels(self) -> None:
        """Load every channel from json file."""
        channels = self.__contents["channels"]

        for channel in channels:
            self.channels.append(Channel(
                channel_id=channel["ChannelId"],
                team_id=channel["TeamId"],
                creator_id=channel["CreatorId"],
                create_at=channel["CreateAt"] or 0,
                delete_at=channel["DeleteAt"] or 0,
                total_msg_count=channel["TotalMsgCount"] or 0,
                post_count=channel["PostCount"] or 0,
                reactions_count=channel["ReactionsCount"] or 0,
                channel_members=[],
                channel_member_history=[]
            ))

    def __load_teams(self) -> None:
        """Load every team from json file."""
        teams = self.__contents["teams"]

        for team in teams:
            self.teams.append(Team(
                team_id=team["TeamId"],
                create_at=team["CreateAt"] or 0,
                delete_at=team["DeleteAt"] or 0,
                invite_only=team["InviteOnly"],
                email_domain_restricted=team["EmailDomainRestricted"],
                channels=[],
                team_members=[]
            ))

    def __load_channel_members(self) -> None:
        """Load every channel member from json file."""
        channel_members = self.__contents["channel_members"]

        for channel_member in channel_members:
            self.channel_members.append(ChannelMember(
                channel_id=channel_member["ChannelId"],
                user_id=channel_member["UserId"],
                msg_count=channel_member["MsgCount"] or 0,
                mention_count=channel_member["MentionCount"] or 0
            ))

    def __load_channel_member_histories(self) -> None:
        """Load every channel member history from json file."""
        channel_member_histories = self.__contents["channel_member_history"]

        for channel_member_history in channel_member_histories:
            self.channel_member_histories.append(ChannelMemberHistoryEntry(
                channel_id=channel_member_history["ChannelId"],
                user_id=channel_member_history["UserId"],
                join_time=channel_member_history["JoinTime"] or 0,
                leave_time=channel_member_history["LeaveTime"] or 0
            ))

    def __load_team_members(self) -> None:
        """Load every team member from json file."""
        team_members = self.__contents["team_members"]

        for team_member in team_members:
            self.team_members.append(TeamMember(
                team_id=team_member["TeamId"],
                user_id=team_member["UserId"],
                delete_at=team_member["DeleteAt"] or 0
            ))

    def __load_users(self) -> None:
        """Load every user from json file."""
        users = self.__contents["users"]

        for user in users:
            # Since some users might be associated with CERN, but do not reside
            # at CERN, they neither have 'building' or 'orgUnit' values. Hence,
            # just treat them as 'external'.
            user_data: UserData = UserData(building=0, org_unit=0)

            if users[user]["building"] != None:
                user_data.building = users[user]["building"]

            if users[user]["orgUnit"] != None:
                user_data.org_unit = users[user]["orgUnit"]

            self.users[user] = user_data

    def __add_channel_member_history_to_channels(self) -> None:
        """Add the history of channel members joining/leaving to the respective channels."""
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

    def __find_team_channels_and_members(self) -> None:
        """Find every channel and team member related to each team, and add it to the team."""
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

        # Add to teams
        for (team_id, channels) in team_channels.items():
            for team in self.teams:
                if team.team_id == team_id:
                    team.team_members = team_members_map.get(team_id)
                    team.channels = channels

    def __find_building_and_org_unit_members(self) -> None:
        """Creates building and organisational membership objects."""

        for (user_id, user_data) in self.users.items():
            bm = self.building_members.get(user_data.building)

            if bm is None:
                self.building_members[user_data.building] = [user_id]
            else:
                self.building_members[user_data.building].append(user_id)

            om = self.org_unit_members.get(user_data.org_unit)

            if om is None:
                self.org_unit_members[user_data.org_unit] = [user_id]
            else:
                self.org_unit_members[user_data.org_unit].append(user_id)

    def __add_remaining_users_user_data(self) -> None:
        """Add remaining users of data set.

        Since the 'users' JSON object only contains information about some users,
        add all other users that we have and treat them as external ones.
        """
        for team in self.teams:
            for team_member in team.team_members:
                if self.users.get(team_member.user_id) is None:
                    self.users[team_member.user_id] = UserData(building=0,
                                                               org_unit=0)
            for channel in team.channels:
                for channel_member in channel.channel_members:
                    if self.users.get(channel_member.user_id) is None:
                        self.users[channel_member.user_id] = UserData(building=0,
                                                                      org_unit=0)

        for channel_member in self.channel_members:
            if self.users.get(channel_member.user_id) is None:
                self.users[channel_member.user_id] = UserData(building=0,
                                                              org_unit=0)

        for channel_member_history in self.channel_member_histories:
            if self.users.get(channel_member_history.user_id) is None:
                self.users[channel_member_history.user_id] = UserData(building=0,
                                                                      org_unit=0)
