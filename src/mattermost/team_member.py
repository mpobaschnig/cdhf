class TeamMember:
    team_id: int
    user_id: int
    delete_at: int

    def __init__(self, team_id: int, user_id: int, delete_at: int):
        self.team_id = team_id
        self.user_id = user_id
        self.delete_at = delete_at
