from typing import List

from .channel import Channel
from .team_member import TeamMember


class Team:
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
        self.team_id = team_id
        self.create_at = create_at
        self.delete_at = delete_at
        self.invite_only = invite_only
        self.email_domain_restricted = email_domain_restricted

        self.channels = channels
        self.team_members = team_members
