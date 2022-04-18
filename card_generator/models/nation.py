from models.alliance import Alliance

class Nation:
    def __init__(self, name: str, alliance: Alliance) -> None:
        self.units = list()
        self.name = name
        self.alliance = alliance

    def getAlliance(self) -> Alliance:
        return self.alliance

    def getName(self) -> str:
        return self.name

    def getUnits(self) -> list:
        return self.units

    def addUnit(self, unit: int) -> None:
        self.units.append(unit)


NATION_LIST = [
    Nation("Australia", Alliance.Allies),
    Nation("United States", Alliance.Allies),
    Nation("Canada", Alliance.Allies),
    Nation("United Kingdom", Alliance.Allies),
    Nation("Soviet Union", Alliance.Allies),
    Nation("France", Alliance.Allies),
    Nation("Germany", Alliance.Axis),
    Nation("Italy", Alliance.Axis),
    Nation("Japan", Alliance.Axis)
]