# channel.py
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

from typing import List, Optional

from .channel_member import ChannelMember
from .channel_member_history_entry import ChannelMemberHistoryEntry


class Channel:
    """Class representing channel information."""
    channel_id: int
    team_id: int
    creator_id: int
    create_at: int
    delete_at: int
    total_msg_count: int
    post_count: int
    reactions_count: int

    # Custom stuff
    channel_members: List[ChannelMember]
    channel_member_history: List[ChannelMemberHistoryEntry]

    def __init__(self, channel_id: int, team_id: int, creator_id: int, create_at: int, delete_at: int, total_msg_count: int, post_count: int, reactions_count: int, channel_members: List[ChannelMember], channel_member_history: List[ChannelMemberHistoryEntry]):
        """
        Args:
            channel_id (int): Channel Identifier
            team_id (int): Team Identifier
            creator_id (int): Creator User Identifier
            create_at (int): Created Timestamp
            delete_at (int): Deleted Timestamp
            total_msg_count (int): Total Channel Message Count
            post_count (int): Total Channel Post Count
            reactions_count (int): Total CHannel Reactions Count
            channel_members (List[ChannelMember]): List of Channel Members
            channel_member_history (List[ChannelMemberHistoryEntry]): List that contains information when users joined of left the Channel
        """
        self.channel_id = channel_id
        self.team_id = team_id
        self.creator_id = creator_id
        self.create_at = create_at
        self.delete_at = delete_at
        self.total_msg_count = total_msg_count
        self.post_count = post_count
        self.reactions_count = reactions_count

        # Custom stuff
        self.channel_members = channel_members
        self.channel_member_history = channel_member_history
