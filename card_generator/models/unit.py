from card_generator.models.nation import Nation


class Unit:
    def __init__(self) -> None:
        self.name = None
        self.nation = None
        self.flagship = None
        self.points = None
        self.year = None
        self.type = None
        self.speed = None
        self.planes = None
        self.main_gunnery_attack = list()
        self.aircraft_gunnery_attack = list()
        self.secondary_gunnery_attack = list()
        self.tertiary_gunnery_attack = list()
        self.anti_aircraft_attack = list()
        self.anti_submarine_attack = list()
        self.torpedo_attack = list()
        self.bomb_attack = list()
        self.armor = None
        self.vital_armor = None
        self.hull_points = None
        self.special_abilities = dict()
        self.set = None
        self.set_number = None
        self.rarity = None

    def with_name(self, name: str):
        self.name = name
        return self

    def with_nation(self, nation: Nation):
        self.nation = nation
        return self

    def with_flagship_value(self, flagship_points: int):
        self.flagship = flagship_points
        return self

    def with_type(self, unit_type: str):
        self.type = unit_type
        return self

    def with_point_value(self, points: int):
        self.points = points
        return self

    def with_year(self, year: int):
        self.year = year
        return self

    def with_speed(self, speed: str):
        self.speed = speed
        return self

    def with_plane_capacity(self, planes: int):
        self.planes = planes
        return self

    def with_main_gunnery_attack(self, attack_vector: list):
        self.main_gunnery_attack = attack_vector
        return self

    def with_aircraft_gunnery_attack(self, attack_vector: list):
        self.aircraft_gunnery_attack = attack_vector
        return self

    def with_secondary_gunnery_attack(self, attack_vector: list):
        self.secondary_gunnery_attack = attack_vector
        return self

    def with_tertiary_gunnery_attack(self, attack_vector: list):
        self.tertiary_gunnery_attack = attack_vector
        return self

    def with_anti_air_attack(self, attack_vector: list):
        self.anti_aircraft_attack = attack_vector
        return self

    def with_anti_submarine_attack(self, attack_vector: list):
        self.anti_submarine_attack = attack_vector
        return self

    def with_torpedo_attack(self, attack_vector: list):
        self.torpedo_attack = attack_vector
        return self

    def with_bomb_attack(self, attack_vector: list):
        self.bomb_attack = attack_vector
        return self

    def with_armor(self, armor: int):
        self.armor = armor
        return self

    def with_vital_armor(self, armor: int):
        self.vital_armor = armor
        return self

    def with_hull_points(self, hull_points: int):
        self.hull_points = hull_points
        return self

    def with_special_abilities(self, abilities: dict):
        self.special_abilities = abilities
        return self

    def with_set(self, game_set: str):
        self.set = game_set
        return self

    def with_set_number(self, set_number: str):
        self.set_number = set_number
        return self

    def with_rarity(self, rarity: str):
        self.rarity = rarity
        return self

    def __str__(self):
        elements = self.__dict__.keys()
        string = ""
        for element in elements:
            string += str(element) + ": " + str(self.__dict__[element]) + "\n"
        return string
