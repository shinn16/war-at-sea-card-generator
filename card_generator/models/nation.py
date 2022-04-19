from card_generator.models.alliance import Alliance


class Nation:
    def __init__(self, name: str, alliance: Alliance) -> None:
        self.units = list()
        self.name = name
        self.alliance = alliance

    def get_alliance(self) -> Alliance:
        return self.alliance

    def get_name(self) -> str:
        return self.name

    def get_units(self) -> list:
        return self.units

    def add_unit(self, unit) -> None:
        self.units.append(unit)

    def __str__(self):
        units_string = ""
        for unit in self.units:
            units_string += str(unit) + "\n"
        string = "Name: {}, Alliance: {}, Units: \n{}".format(self.name, self.alliance, units_string)
        return string


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
