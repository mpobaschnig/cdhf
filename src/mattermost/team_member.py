# team_member.py
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

class TeamMember:
    """ Class Representing Team Membership
    """
    team_id: int
    user_id: int
    delete_at: int

    def __init__(self, team_id: int, user_id: int, delete_at: int):
        """

        Args:
            team_id (int): Team identifier
            user_id (int): User identifier
            delete_at (int): Describes the timestamp when the user left the team with the team_id
        """
        self.team_id = team_id
        self.user_id = user_id
        self.delete_at = delete_at
