import json
import numpy as np

from typing import Dict, List, Optional

from .channel import Channel
from .channel_member import ChannelMember
from .channel_member_history_entry import ChannelMemberHistoryEntry
from .team_member import TeamMember
from .team import Team
from .user_data import UserData


class Preprocessor:
    contents: Optional[str]

    channels: List[Channel]
    channel_members: List[ChannelMember]
    channel_member_histories: List[ChannelMemberHistoryEntry]
    team_members: List[TeamMember]
    teams: List[Team]
    users: Dict[int, UserData]

    building_members: Dict[str, List[str]] = {}
    org_unit_members: Dict[str, List[str]] = {}
    
    __building_smap_c: int
    __building_smap: Dict[str, int]
    __channel_id_subst_map_c: int
    __channel_id_subst_map: Dict[str, int]
    __creator_id_smap_c: int
    __creator_id_smap: Dict[str, int]
    __org_unit_smap_c: int
    __org_unit_smap: Dict[str, int]
    __team_id_smap_c: int
    __team_id_smap: Dict[str, int]
    __user_id_smap_c: int
    __user_id_smap: Dict[str, int]

    def __init__(self, data_file_path: str):
        self.channels = []
        self.channel_members = []
        self.channel_member_histories = []
        self.team_members = []
        self.teams = []
        self.users = {}

        # We start id counters with 1 where 0 is reserved for external persons
        self.__building_smap_c = 1
        self.__building_smap: Dict[str, int] = {}
        self.__channel_id_subst_map_c = 0
        self.__channel_id_subst_map: Dict[str, int] = {}
        self.__creator_id_smap_c = 0
        self.__creator_id_smap: Dict[str, int] = {}
        self.__org_unit_smap_c = 1
        self.__org_unit_smap: Dict[str, int] = {}
        self.__team_id_smap_c = 0
        self.__team_id_smap: Dict[str, int] = {}
        self.__user_id_smap_c = 0
        self.__user_id_smap: Dict[str, int] = {}

    def load_all(self) -> None:
        """
        Load everything from the content file into their variables,
        then free the content memory.
        """

        with open("input/mmdata.json") as f:
            self.contents = json.load(f)

        self.load_channels()
        self.load_channel_members()
        self.load_channel_member_histories()
        self.load_team_members()
        self.load_users()

        self.add_channel_member_history_to_channels()

        self.find_team_channels_and_members()

        self.find_building_members()

        self.cleanup()

    def __subst(self, map, old_id, c):
        new_id = map.get(old_id)
        if new_id is None:
            new_id = c
            map[old_id] = new_id
            c += 1
        return (map, new_id, c)

    def __add0(self, value) -> Optional[int]:
        if value is not None:
            return value + 0
        else:
            return value

    def load_channels(self) -> None:
        """
        Load every channel from json file.
        """
        channels = self.contents["channels"]

        for channel in channels:
            (self.__channel_id_subst_map, channel_id, self.__channel_id_subst_map_c) = self.__subst(self.__channel_id_subst_map,
                                                                                                    channel["ChannelId"], self.__channel_id_subst_map_c)

            (self.__team_id_smap, team_id, self.__team_id_smap_c) = self.__subst(
                self.__team_id_smap, channel["TeamId"], self.__team_id_smap_c)

            (self.__creator_id_smap, creator_id, self.__creator_id_smap_c) = self.__subst(
                self.__creator_id_smap, channel["CreatorId"], self.__creator_id_smap_c)

            self.channels.append(Channel(
                channel_id=channel_id,
                team_id=team_id,
                creator_id=creator_id,
                create_at=self.__add0(channel["CreateAt"]),
                delete_at=self.__add0(channel["DeleteAt"]),
                total_msg_count=self.__add0(channel["TotalMsgCount"]),
                post_count=self.__add0(channel["PostCount"]),
                reactions_count=self.__add0(channel["ReactionsCount"]),
                channel_members=[],
                channel_member_history=[]
            ))

    def load_channel_members(self) -> None:
        """
        Load every channel member from json file.
        """
        channel_members = self.contents["channel_members"]

        for channel_member in channel_members:
            (self.__channel_id_subst_map, channel_id, self.__channel_id_subst_map_c) = self.__subst(self.__channel_id_subst_map,
                                                                                                    channel_member["ChannelId"], self.__channel_id_subst_map_c)

            (self.__user_id_smap, user_id, self.__user_id_smap_c) = self.__subst(
                self.__user_id_smap, channel_member["UserId"], self.__user_id_smap_c)

            self.channel_members.append(ChannelMember(
                channel_id=channel_id,
                user_id=user_id,
                msg_count=self.__add0(channel_member["MsgCount"]),
                mention_count=self.__add0(channel_member["MentionCount"])
            ))

    def load_channel_member_histories(self) -> None:
        """
        Load every channel member history from json file.
        """
        channel_member_histories = self.contents["channel_member_history"]

        for channel_member_history in channel_member_histories:
            (self.__channel_id_subst_map, channel_id, self.__channel_id_subst_map_c) = self.__subst(self.__channel_id_subst_map,
                                                                                                    channel_member_history["ChannelId"], self.__channel_id_subst_map_c)

            (self.__user_id_smap, user_id, self.__user_id_smap_c) = self.__subst(
                self.__user_id_smap, channel_member_history["UserId"], self.__user_id_smap_c)

            self.channel_member_histories.append(ChannelMemberHistoryEntry(
                channel_id=channel_id,
                user_id=user_id,
                join_time=self.__add0(channel_member_history["JoinTime"]),
                leave_time=self.__add0(channel_member_history["LeaveTime"])
            ))

        del channel_member_histories

    def load_team_members(self) -> None:
        """
        Load every team member from json file.
        """
        team_members = self.contents["team_members"]

        for team_member in team_members:
            (self.__team_id_smap, team_id, self.__team_id_smap_c) = self.__subst(
                self.__team_id_smap, team_member["TeamId"], self.__team_id_smap_c)

            (self.__user_id_smap, user_id, self.__user_id_smap_c) = self.__subst(
                self.__user_id_smap, team_member["UserId"], self.__user_id_smap_c)

            self.team_members.append(TeamMember(
                team_id=team_id,
                user_id=user_id,
                delete_at=self.__add0(team_member["DeleteAt"])
            ))

    def load_users(self) -> None:
        """
        Load every user from json file.
        """
        users = self.contents["users"]

        for user in users:
            user_id = self.__user_id_smap.get(user)

            # Since some users might be associated with CERN, but do not reside
            # at CERN, they neither have 'building' or 'orgUnit' values. Hence,
            # just treat them as 'external'.
            if user_id is None:
                self.users[user_id] = UserData(building=0, org_unit=0)
            else:
                (self.__building_smap, building_id, self.__building_smap_c) = self.__subst(
                    self.__building_smap, users[user]["building"], self.__building_smap_c)

                (self.__org_unit_smap, org_unit_id, self.__org_unit_smap_c) = self.__subst(
                    self.__org_unit_smap, users[user]["orgUnit"], self.__org_unit_smap_c)

                self.users[user_id] = UserData(
                    building=building_id, org_unit=org_unit_id)

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

    def find_building_members(self):
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

    def cleanup(self):
        """
        Release the memory of unneeded variables
        """
        import gc

        del self.contents
        del self.__building_smap
        del self.__channel_id_subst_map
        del self.__creator_id_smap
        del self.__org_unit_smap
        del self.__team_id_smap
        del self.__user_id_smap

        gc.collect()
