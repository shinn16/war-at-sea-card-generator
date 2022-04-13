from PIL import Image, ImageFont

DIVIDER_SPACING = 76


class Values:
    # card positions
    LEFT_CARD_BORDER = 56

    # specific elements
    ATTACK_HEADER_Y_END = 296

    ATTACK_RECTANGLE_START_Y = 295
    ATTACK_RECTANGLE_START_X = 210
    ATTACK_RECTANGLE_END_X = 513
    ATTACK_RECTANGLE_WIDTH = 55

    ATTACK_VERTICAL_DIVIDER_1 = 286
    ATTACK_VERTICAL_DIVIDER_2 = ATTACK_VERTICAL_DIVIDER_1 + DIVIDER_SPACING
    ATTACK_VERTICAL_DIVIDER_3 = ATTACK_VERTICAL_DIVIDER_2 + DIVIDER_SPACING

    ARMOR_ROW_TOP_MARGIN = 15
    ARMOR_ROW_HEIGHT = 45
    ARMOR_ROW_WIDTH = 630


class BackgroundAssets:
    HITPOINTS = Image.open("assets/hitpoints.png").resize((44,44))


class Resizing:
    NATION_EMBLEM = (60, 60)


class Icons:
    GUNNERY_1 = Image.open("assets/card-icons/Gunnery1-Ship.png")
    GUNNERY_2 = Image.open("assets/card-icons/Gunnery2.png")
    GUNNERY_3 = Image.open("assets/card-icons/Gunnery3.png")
    ANTI_AIR = Image.open("assets/card-icons/Antiair.png")
    TORPEDO = Image.open("assets/card-icons/Torpedo.png")
    AIRCRAFT_GUNNERY = Image.open("assets/card-icons/Gunnery1-Aircraft.png")
    BOMBS = Image.open("assets/card-icons/Bomb.png")

    CARRIER = Image.open("assets/card-icons/Carrier.png")
    FLAGSHIP = Image.open("assets/card-icons/Flagship.png")


class NationEmblems:
    GERMANY = Image.open("assets/nation-emblems/Germany-sm.png").resize(Resizing.NATION_EMBLEM)
    ITALY = Image.open("assets/nation-emblems/Italy-sm.png").resize(Resizing.NATION_EMBLEM)
    JAPAN = Image.open("assets/nation-emblems/Japan-sm.png").resize(Resizing.NATION_EMBLEM)
    US = Image.open("assets/nation-emblems/United States-sm.png").resize(Resizing.NATION_EMBLEM)
    UK = Image.open("assets/nation-emblems/United Kingdom-sm.png").resize(Resizing.NATION_EMBLEM)
    CANADA = Image.open("assets/nation-emblems/Canada-sm.png").resize(Resizing.NATION_EMBLEM)
    AUSTRALIA = Image.open("assets/nation-emblems/Australia-sm.png").resize(Resizing.NATION_EMBLEM)
    FRANCE = Image.open("assets/nation-emblems/France-sm.png").resize(Resizing.NATION_EMBLEM)
    GREECE = Image.open("assets/nation-emblems/Greece-sm.png").resize(Resizing.NATION_EMBLEM)
    NETHERLANDS = Image.open("assets/nation-emblems/Netherlands-sm.png").resize(Resizing.NATION_EMBLEM)
    SWEDEN = Image.open("assets/nation-emblems/Sweden-sm.png").resize(Resizing.NATION_EMBLEM)
    USSR = Image.open("assets/nation-emblems/Soviet Union-sm.png").resize(Resizing.NATION_EMBLEM)
    FINLAND = Image.open("assets/nation-emblems/Finland-sm.png").resize(Resizing.NATION_EMBLEM)
    NEW_ZEALAND = Image.open("assets/nation-emblems/New Zealand-sm.png").resize(Resizing.NATION_EMBLEM)


class Colors:
    TRANSPARENT = (255, 255, 255, 0)
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    GREY = (137, 140, 141)
    SHIP_NAME = WHITE
    POINT_VALUE = WHITE
    SHIP_TYPE_AND_YEAR = (134, 135, 137)
    STATS = WHITE
    ATTACK_VALUE_BACKGROUND = (0, 255, 0, 80) # transparent green


class Fonts:
    SHIP_NAME = ImageFont.truetype("assets/Komet - Flicker - B52-Regular.ttf", 75)
    POINT_VALUE = ImageFont.truetype("assets/Komet - Flicker - B52-Regular.ttf", 94)
    SHIP_TYPE_AND_YEAR = ImageFont.truetype("assets/Komet - Flicker - B52-Regular.ttf", 30)
    SHIP_SPEED = ImageFont.truetype("assets/Komet - Flicker - B52-Regular.ttf", 35)
    ATTACK_ARMOR_STATS_HEADINGS = ImageFont.truetype("assets/Komet - Flicker - B52-Regular.ttf", 30)
    ATTACK_ARMOR_STATS = ImageFont.truetype("assets/Komet - Flicker - B52-Regular.ttf", 70)


class Coordinates:
    NATION_EMBLEM = (45, 165)
    SHIP_NAME = (78, 91)
    SINGLE_DIGIT_POINT_VALUE = (625, 84)
    DOUBLE_DIGIT_POINT_VALUE = (597, 84)
    SHIP_TYPE = (128, 165)
    SHIP_YEAR = (510, 165)
    SHIP_SPEED = (130, 206)

    ATTACK_HEADING = (72, 257)
    ATTACK_RANGE_HEADING_0 = (240, ATTACK_HEADING[1])
    ATTACK_RANGE_HEADING_1 = (ATTACK_RANGE_HEADING_0[0] + 77, ATTACK_HEADING[1])
    ATTACK_RANGE_HEADING_2 = (ATTACK_RANGE_HEADING_1[0] + 74, ATTACK_HEADING[1])
    ATTACK_RANGE_HEADING_3 = (ATTACK_RANGE_HEADING_2[0] + 74, ATTACK_HEADING[1])

    ATTACK_HEADING_DIVIDER = [(210, 254), (210, 292)]
    ATTACK_HEADING_DIVIDER_1 = [
        (ATTACK_HEADING_DIVIDER[0][0] + DIVIDER_SPACING, ATTACK_HEADING_DIVIDER[0][1]),
        (ATTACK_HEADING_DIVIDER[1][0] + DIVIDER_SPACING, ATTACK_HEADING_DIVIDER[1][1])
    ]
    ATTACK_HEADING_DIVIDER_2 = [
        (ATTACK_HEADING_DIVIDER_1[0][0] + DIVIDER_SPACING, ATTACK_HEADING_DIVIDER[0][1]),
        (ATTACK_HEADING_DIVIDER_1[1][0] + DIVIDER_SPACING, ATTACK_HEADING_DIVIDER[1][1])
    ]
    ATTACK_HEADING_DIVIDER_3 = [
        (ATTACK_HEADING_DIVIDER_2[0][0] + DIVIDER_SPACING, ATTACK_HEADING_DIVIDER[0][1]),
        (ATTACK_HEADING_DIVIDER_2[1][0] + DIVIDER_SPACING, ATTACK_HEADING_DIVIDER[1][1])
    ]
