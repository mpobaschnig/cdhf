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

from typing import Dict, List, Optional

from .channel import Channel
from .channel_member import ChannelMember
from .channel_member_history_entry import ChannelMemberHistoryEntry
from .team_member import TeamMember
from .team import Team
from .user_data import UserData


class Data:
    """A class used for processing and holding the data set"""
    file_path: Optional[str]
    """Path to the Mattermost JSON file."""

    __contents: Optional[str]
    """Content of the Mattermost JSON file."""

    channels: List[Channel]
    """List of all channels."""
    channel_members: List[ChannelMember]
    """List of all channel members."""
    channel_member_history: List[ChannelMemberHistoryEntry]
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

    def __init__(self, file_path: str):
        """
        Args:
            file_path (str): Path to Mattermost data set JSON file.
        """
        self.channels = []
        self.channel_members = []
        self.channel_member_history = []
        self.team_members = []
        self.teams = []
        self.users = {}

        self.file_path = file_path

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
        self.__attach_team_channels_and_members()
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
                create_at=channel["CreateAt"],
                delete_at=channel["DeleteAt"],
                total_msg_count=channel["TotalMsgCount"],
                post_count=channel["PostCount"],
                reactions_count=channel["ReactionsCount"],
                channel_members=[],
                channel_member_history=[]
            ))

    def __load_teams(self) -> None:
        """Load every team from json file."""
        teams = self.__contents["teams"]

        for team in teams:
            self.teams.append(Team(
                team_id=team["TeamId"],
                create_at=team["CreateAt"],
                delete_at=team["DeleteAt"],
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
                msg_count=channel_member["MsgCount"],
                mention_count=channel_member["MentionCount"]
            ))

    def __load_channel_member_histories(self) -> None:
        """Load every channel member history from json file."""
        channel_member_histories = self.__contents["channel_member_history"]

        for channel_member_history in channel_member_histories:
            self.channel_member_history.append(ChannelMemberHistoryEntry(
                channel_id=channel_member_history["ChannelId"],
                user_id=channel_member_history["UserId"],
                join_time=channel_member_history["JoinTime"],
                leave_time=channel_member_history["LeaveTime"]
            ))

    def __load_team_members(self) -> None:
        """Load every team member from json file."""
        team_members = self.__contents["team_members"]

        for team_member in team_members:
            self.team_members.append(TeamMember(
                team_id=team_member["TeamId"],
                user_id=team_member["UserId"],
                delete_at=team_member["DeleteAt"]
            ))

    def __load_users(self) -> None:
        """Load every user from json file."""
        users = self.__contents["users"]

        for user in users:
            self.users[user] = UserData(building=users[user]["building"],
                                        org_unit=users[user]["orgUnit"])

    def __add_channel_member_history_to_channels(self) -> None:
        """Add the history of channel members joining/leaving to the respective channels."""
        channel_history: Dict[str, List[ChannelMemberHistoryEntry]] = {}
        for h_entry in self.channel_member_history:
            h_list = channel_history.get(h_entry.channel_id, [])
            h_list.append(h_entry)
            channel_history[h_entry.channel_id] = h_list

        for channel in self.channels:
            h_list = channel_history.get(channel.channel_id, [])
            channel.channel_member_history = h_list

    def __attach_team_channels_and_members(self) -> None:
        """Attach channel members to channels and team members/channels to teams."""
        channel_members: Dict[str, List[ChannelMember]] = {}
        for channel_member in self.channel_members:
            cm_list = channel_members.get(channel_member.channel_id, [])
            cm_list.append(channel_member)
            channel_members[channel_member.channel_id] = cm_list

        team_channels: Dict[str, List[Channel]] = {}
        for channel in self.channels:
            cm_list = channel_members.get(channel.channel_id, [])
            channel.channel_members = cm_list

            tc_list = team_channels.get(channel.team_id, [])
            tc_list.append(channel)
            team_channels[channel.team_id] = tc_list

        team_members: Dict[str, List[TeamMember]] = {}
        for team_member in self.team_members:
            tm_list = team_members.get(team_member.team_id, [])
            tm_list.append(team_member)
            team_members[team_member.team_id] = tm_list

        for team in self.teams:
            team.channels = team_channels.get(team.team_id, [])
            team.team_members = team_members.get(team.team_id, [])

    def __find_building_and_org_unit_members(self) -> None:
        """Creates building and organisational membership objects."""

        for (user_id, user_data) in self.users.items():
            m_list = self.building_members.get(user_data.building, [])
            m_list.append(user_id)
            self.building_members[user_data.building] = m_list

            m_list = self.org_unit_members.get(user_data.org_unit, [])
            m_list.append(user_id)
            self.org_unit_members[user_data.org_unit] = m_list

    def __add_remaining_users_user_data(self) -> None:
        """Add remaining users of data set.

        Since the 'users' JSON object only contains information about some users,
        add all other users that we have and treat them as external ones.
        """
        for team in self.teams:
            for team_member in team.team_members:
                if self.users.get(team_member.user_id) is None:
                    self.users[team_member.user_id] = UserData(building="",
                                                               org_unit="")
        for channel_member in self.channel_members:
            if self.users.get(channel_member.user_id) is None:
                self.users[channel_member.user_id] = UserData(building="",
                                                              org_unit="")

        for channel_member_history in self.channel_member_history:
            if self.users.get(channel_member_history.user_id) is None:
                self.users[channel_member_history.user_id] = UserData(building="",
                                                                      org_unit="")
