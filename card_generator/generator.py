import enum


class TextColor(enum.Enum):
    SHIP_NAME = (255, 255, 255)
    POINT_VALUE = (255, 255, 255)
    SHIP_TYPE_AND_YEAR = (134, 135, 137)
    STATS = (255, 255, 255)


class TextSize(enum.Enum):
    SHIP_NAME = 50
    POINT_VALUE = 94
    SHIP_TYPE_AND_YEAR = 30
    SHIP_SPEED = 35
    ATTACK_ARMOR_STATS = 30


class Resizing(enum.Enum):
    NATION_EMBLEM = (60, 60)


class Coordinates(enum.Enum):
    NATION_EMBLEM = (51, 135)
    SHIP_NAME = (78, 78)
    SINGLE_DIGIT_POINT_VALUE = (625, 52)
    DOUBLE_DIGIT_POINT_VALUE = (597, 52)
    SHIP_TYPE = (128, 133)
    SHIP_YEAR = (510, 133)
    SHIP_SPEED = (130, 174)


class CardGenerator:

    def __init__(self):
        pass

