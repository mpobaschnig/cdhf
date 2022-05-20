# channel_member_history_entry.py
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

from typing import Optional


class ChannelMemberHistoryEntry:
    channel_id: int
    user_id: int
    join_time: int
    leave_time: Optional[int]

    def __init__(self, channel_id: int, user_id: int, join_time: int, leave_time: Optional[int]):
        """

        Args:
            channel_id (int): Channel Identifier
            user_id (int): User Identifier
            join_time (int): Timestamp when the user with user_id joined the chennel with the channel_id
            leave_time (Optional[int]): Timestamp when the user with user_id left the chennel with the channel_id
        """
        self.channel_id = channel_id
        self.user_id = user_id
        self.join_time = join_time
        self.leave_time = leave_time
