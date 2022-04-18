from models.nation import Nation

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
        self.secondary_gunnary_attack = list()
        self.tertiary_gunnery_attack = list()
        self.anti_aircraft_attack = list()
        self.anti_submarine_attack = list()
        self.torpedo_attack = list()
        self.bomb_attack = list()
        self.armor = None
        self.vital_armor = None
        self.hull_points = None
        self.special_abilties = dict()
        self.set = None
        self.set_number = None
        self.rarity = None

    def withName(self, name: str) -> None:
        self.name = name
        

    def withNation(self, nation: Nation) -> None:
        self.nation = nation
        

    def withFlagShipValue(self, flagship_points: int) -> None:
        self.flagship = flagship_points
        

    def withType(self, type: str) -> None:
        self.type = type

    def withPointValue(self, points: int) -> None:
        self.points = points
        

    def withYear(self, year: int) -> None:
        self.year = year
        

    def withSpeed(self, speed: str) -> None:
        self.speed = speed
        

    def withPlaneCapacity(self, planes: int) -> None:
        self.planes = planes

    def withMainGunneryAttack(self, attackVector: list) -> None:
        self.main_gunnery_attack = attackVector
        

    def withAircraftGunneryAttack(self, attackVector: list) -> None:
        self.aircraft_gunnery_attack = attackVector

    def withSecondaryGunneryAttack(self, attackVector: list) -> None:
        self.secondary_gunnary_attack = attackVector
        

    def withTertiaryGunneryAttack(self, attackVector: list) -> None:
        self.tertiary_gunnery_attack = attackVector
        

    def withAntiAirAttack(self, attackVector: list) -> None:
        self.anti_aircraft_attack = attackVector
        

    def withAntiSubmarineAttack(self, attackVector: list) -> None:
        self.anti_submarine_attack = attackVector
        

    def withTorpedoAttack(self, attackVector: list) -> None:
        self.torpedo_attack = attackVector
        

    def withBombAttack(self, attackVector: list) -> None:
        self.bomb_attack = attackVector

    def withArmor(self, armor: int) -> None:
        self.armor = armor
        

    def withVitalArmor(self, armor: int) -> None:
        self.vital_armor = armor
        
    
    def withHullPoints(self, hull_points: int) -> None:
        self.hull_points = hull_points
        

    def withSpecialAbilities(self, abilites: dict) -> None:
        self.special_abilties = abilites
        

    def withSet(self, set: str) -> None:
        self.set = set
    
    def withSetNumber(self, setNumber: str) -> None:
        self.set_number = setNumber

    def withRarity(self, rarity: str) -> None:
        self.rarity = rarity

    def __str__(self):
        elements = self.__dict__.keys()
        string = ""
        for element in elements:
            string += str(element) + ": " + str(self.__dict__[element]) + "\n"
        return string

