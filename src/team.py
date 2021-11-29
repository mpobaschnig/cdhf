from typing import List

from channel import Channel
from team_member import TeamMember


class Team:
    team_id: str
    channels: List[Channel]
    team_members: List[TeamMember]

    def __init__(self, team_id: str, channels: List[Channel], team_members: List[TeamMember]) -> None:
        self.team_id = team_id
        self.channels = channels
        self.team_members = team_members
