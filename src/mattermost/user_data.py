class UserData:
    building: int
    org_unit: int

    def __init__(self, building: int, org_unit: int) -> None:
        self.building = building
        self.org_unit = org_unit
