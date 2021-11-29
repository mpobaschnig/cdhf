class TeamMember:
    team_id: str
    user_id: str
    delete_at: int

    def __init__(self, team_id: str, user_id: str, delete_at: int):
        self.team_id = team_id
        self.user_id = user_id
        self.delete_at = delete_at
