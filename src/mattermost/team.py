from typing import List

from .channel import Channel
from .team_member import TeamMember


class Team:
    """ Class Representation of Mattermost Team
    """
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
            team_id (int): Team Identifier
            create_at (int): Created Timestamp
            delete_at (int): Deleted Timestamp
            invite_only (bool): Describes if users can join the team with invitaion or public
            email_domain_restricted (bool): Describes if the team is restricted to an email domain or public
            channels (List[Channel]): List of Channels that are part of the Mattermost Team
            team_members (List[TeamMember]): Users that are assigned to the team
        """
         

        self.team_id = team_id
        self.create_at = create_at
        self.delete_at = delete_at
        self.invite_only = invite_only
        self.email_domain_restricted = email_domain_restricted

        self.channels = channels
        self.team_members = team_members
