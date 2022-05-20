# channel_member.py
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

class ChannelMember:
    channel_id: int
    user_id: int
    msg_count: int
    mention_count: int

    def __init__(self, channel_id: int, user_id: int, msg_count: int, mention_count: int):
        """
        Args:
            channel_id (int): Channel Identifier
            user_id (int): User Identifier
            msg_count (int): Total Message Count of User with user_id in Channel with channel_id
            mention_count (int):  Total Mentions of User with user_id in Channel with channel_id
        """
        self.channel_id = channel_id
        self.user_id = user_id
        self.msg_count = msg_count
        self.mention_count = mention_count
