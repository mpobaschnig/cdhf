class UserData:
    """ Class Representing Basic User Informations
    """
    building: int
    org_unit: int

    def __init__(self, building: int, org_unit: int) -> None:
        """
        Args:
            building (int): Users' Building Identifier
            org_unit (int): Users' Organisational Identifier
        """
        self.building = building
        self.org_unit = org_unit
