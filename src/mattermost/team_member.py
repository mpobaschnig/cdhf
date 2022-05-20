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
