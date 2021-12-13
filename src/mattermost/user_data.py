class UserData:
    building: str
    org_unit: str

    def __init__(self, building: str, org_unit: str) -> None:
        self.building = building
        self.org_unit = org_unit
