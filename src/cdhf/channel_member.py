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
    channel_id: str
    user_id: str
    msg_count: int
    mention_count: int

    def __init__(self, channel_id: str, user_id: str, msg_count: int, mention_count: int):
        """
        Args:
            channel_id (str): Channel identifier.
            user_id (str): User identifier.
            msg_count (int): Total message count of user with user_id in channel with channel_id.
            mention_count (int):  Total mentions of user with user_id in channel with channel_id.
        """
        self.channel_id = channel_id
        self.user_id = user_id
        self.msg_count = msg_count
        self.mention_count = mention_count
