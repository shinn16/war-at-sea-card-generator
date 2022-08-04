import enum


class UnitType(enum.Enum):
    SHIP = 0,
    PLANE = 1


class BlueprintSettings:
    def __init__(self, settings: dict):
        """
        Creates optional settings
        :param settings:
        :return:
        """
        fields = ["max_width", "x_placement", "y_placement", "file_name",
                  "back_max_width", "back_x_placement, back_y_placement"]
        for field in fields:
            try:
                self.__setattr__(field, settings[field])
            except KeyError:
                self.__setattr__(field, None)


class Unit:
    def __init__(self):
        self.name = None
        # self.nation = None
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
        self.ship_class = None
        self.manufacturer = None
        self.blue_print_settings = None
        self.back_text = ""

    def with_name(self, name: str):
        self.name = name
        return self

    # def with_nation(self, nation: Nation):
    #     self.nation = nation
    #     return self

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

    def with_ship_class(self, ship_class: str):
        self.ship_class = ship_class
        return self

    def with_blueprint_settings(self, settings: dict):
        self.blue_print_settings = BlueprintSettings(settings)
        return self

    def with_manufacturer(self, manufacturer: str):
        self.manufacturer = manufacturer
        return this

    def with_back_text(self, text: str):
        self.back_text = text
        return self

    def get_attacks(self) -> tuple:
        number_of_attacks = 0
        attacks = list()
        if len(self.aircraft_gunnery_attack) > 0:
            number_of_attacks += 1
            attacks.append({"name": "aircraft_gunnery", "value": self.aircraft_gunnery_attack})
        if len(self.main_gunnery_attack) > 0:
            number_of_attacks += 1
            attacks.append({"name": "main_gunnery", "value": self.main_gunnery_attack})
        if len(self.secondary_gunnery_attack) > 0:
            number_of_attacks += 1
            attacks.append({"name": "secondary_gunnery", "value": self.secondary_gunnery_attack})
        if len(self.tertiary_gunnery_attack) > 0:
            number_of_attacks += 1
            attacks.append({"name": "tertiary_gunnery", "value": self.tertiary_gunnery_attack})
        if len(self.anti_aircraft_attack) > 0:
            number_of_attacks += 1
            attacks.append({"name": "anti-air", "value": self.anti_aircraft_attack})
        if len(self.bomb_attack) > 0:
            number_of_attacks += 1
            attacks.append({"name": "bomb", "value": self.bomb_attack})
        if len(self.anti_submarine_attack) > 0:
            number_of_attacks += 1
            attacks.append({"name": "asw", "value": self.anti_submarine_attack})
        if len(self.torpedo_attack) > 0:
            number_of_attacks += 1
            attacks.append({"name": "torpedo", "value": self.torpedo_attack})
        return number_of_attacks, attacks

    def get_armor(self) -> dict:
        return {
            "ARMOR": str(self.armor),
            "VITAL ARMOR": str(self.vital_armor),
            "HULL POINTS": str(self.hull_points)
        }

    def __str__(self):
        elements = self.__dict__.keys()
        string = ""
        for element in elements:
            string += str(element) + ": " + str(self.__dict__[element]) + "\n"
        return string
