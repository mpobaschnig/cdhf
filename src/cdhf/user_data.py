# user_data.py
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

class UserData:
    """Class representing basic user information"""
    building: str
    org_unit: str

    def __init__(self, building: str, org_unit: str) -> None:
        """
        Args:
            building (str): Users' Building Identifier
            org_unit (str): Users' Organisational Identifier
        """
        self.building = building
        self.org_unit = org_unit
