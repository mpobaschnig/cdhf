# team.py
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

from typing import List

from .channel import Channel
from .team_member import TeamMember


class Team:
    """Class representation of Mattermost team."""
    team_id: int
    create_at: int
    delete_at: int
    invite_only: bool
    email_domain_restricted: bool

    # Custom Stuff
    channels: List[Channel]
    team_members: List[TeamMember]

    def __init__(self,
                 team_id: int,
                 create_at: int,
                 delete_at: int,
                 invite_only: bool,
                 email_domain_restricted: bool,
                 channels: List[Channel],
                 team_members: List[TeamMember]) -> None:
        """
        Args:
            team_id (int): Team identifier.
            create_at (int): Created timestamp.
            delete_at (int): Deleted timestamp.
            invite_only (bool): Describes if users can join the team with invitaion or public.
            email_domain_restricted (bool): Describes if the team is restricted to an email domain or public.
            channels (List[Channel]): List of channels that are part of the Mattermost team.
            team_members (List[TeamMember]): Users that are assigned to the team.
        """
        self.team_id = team_id
        self.create_at = create_at
        self.delete_at = delete_at
        self.invite_only = invite_only
        self.email_domain_restricted = email_domain_restricted

        self.channels = channels
        self.team_members = team_members
