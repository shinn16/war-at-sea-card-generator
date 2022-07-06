from PIL import ImageFont
from card_generator.models.nation import Nation
from card_generator.utils.helper_functions import *


class Values:
    """
    Variety of values relating to element placement.
    """
    # card positions
    LEFT_CARD_BORDER = 56

    # ship name
    SHIP_NAME_START_X = 78
    SHIP_NAME_END_X = 575
    SHIP_NAME_START_Y = 97
    SHIP_NAME_END_Y = 159
    SHIP_NAME_FONT_TRACKING = -125

    # flagship icon
    FLAGSHIP_CENTER_OFFSET = 40
    FLAGSHIP_VALUE_Y = 209

    # carrier icons
    CARRIER_START_X = 381
    CARRIER_END_X = 500
    CARRIER_Y = 206
    CARRIER_ICON_SPACING = 38

    # border thicknesses
    BORDER_WIDTH = 3

    # specific elements
    ATTACK_HEADER_Y_END = 296

    # card stats and info placement
    ATTACK_RECTANGLE_START_Y = 295
    ATTACK_RECTANGLE_START_X = 170
    ATTACK_RECTANGLE_END_X = 513
    ATTACK_RECTANGLE_WIDTH = 55

    DIVIDER_SPACING = (ATTACK_RECTANGLE_END_X - ATTACK_RECTANGLE_START_X) / 4

    ATTACK_VERTICAL_DIVIDER_1 = ATTACK_RECTANGLE_START_X + DIVIDER_SPACING
    ATTACK_VERTICAL_DIVIDER_2 = ATTACK_VERTICAL_DIVIDER_1 + DIVIDER_SPACING
    ATTACK_VERTICAL_DIVIDER_3 = ATTACK_VERTICAL_DIVIDER_2 + DIVIDER_SPACING

    ARMOR_ROW_TOP_MARGIN = 10
    ARMOR_ROW_HEIGHT = 45
    ARMOR_ROW_WIDTH = 630
    ARMOR_TEXT_LEFT_MARGIN = 6
    ARMOR_TEXT_RIGHT_MARGIN = 5

    SPECIAL_ABILITY_LEFT_MARGIN = 90
    SPECIAL_ABILITY_BOTTOM_MARGIN = 10
    SPECIAL_ABILITY_TOP_MARGIN = 10
    SPECIAL_ABILITY_TEXT_WIDTH = 50

    SET_Y_OFFSET = 990


class Resizing:
    NATION_EMBLEM = (61, 61)
    HIT_POINTS = (44, 44)
    FLAGSHIP = (33, 33)
    CARRIER = (33, 33)


class BackgroundAssets:
    HIT_POINTS = Image.open("card_generator/assets/hitpoints.png").resize(Resizing.HIT_POINTS)


class Icons:
    # attack icons
    ATTACK_ICONS = {
        "aircraft_gunnery": Image.open("card_generator/assets/card-icons/Gunnery1-Aircraft.png"),
        "main_gunnery": icon_resize(Image.open("card_generator/assets/card-icons/Gunnery1-Ship.png"), 0.8),
        "secondary_gunnery": icon_resize(Image.open("card_generator/assets/card-icons/Gunnery2.png"), 0.7),
        "tertiary_gunnery": icon_resize(Image.open("card_generator/assets/card-icons/Gunnery3.png"), 0.6),
        "anti-air": Image.open("card_generator/assets/card-icons/Antiair.png"),
        "bomb": Image.open("card_generator/assets/card-icons/Bomb.png"),
        "asw": Image.open("card_generator/assets/card-icons/ASW.png"),
        "torpedo": Image.open("card_generator/assets/card-icons/Torpedo.png")
    }

    SET_ICONS = {
        "Starter Set": Image.open("card_generator/assets/card-icons/Flagship.png").resize((30, 30)),
        "War At Sea": Image.open("card_generator/assets/card-icons/war_at_sea.png").resize((30, 30)),
        "Task Force": Image.open("card_generator/assets/card-icons/task_force.png").resize((30, 30)),
        "Flank Speed":  Image.open("card_generator/assets/card-icons/flank_speed.png").resize((30, 30)),
        "Condition Zebra": Image.open("card_generator/assets/card-icons/condition_zebra.png").resize((30, 30)),
        "Set V": Image.open("card_generator/assets/card-icons/set V.png").resize((30, 30)),
        "Surface Action": Image.open("card_generator/assets/card-icons/surface_action.png").resize((30, 30))
    }

    # special icons
    CARRIER = Image.open("card_generator/assets/card-icons/Carrier.png").resize(Resizing.CARRIER)
    FLAGSHIP = Image.open("card_generator/assets/card-icons/Flagship.png").resize(Resizing.FLAGSHIP)

    # rarity icons
    RARE = Image.open("card_generator/assets/card-icons/rare.png").resize((30, 30))
    UNCOMMON = Image.open("card_generator/assets/card-icons/uncommon.png").resize((30, 30))
    COMMON = Image.open("card_generator/assets/card-icons/common.png").resize((30, 30))


class NationEmblems:
    GERMANY = Image.open("card_generator/assets/nation-emblems/Germany-sm.png").resize(Resizing.NATION_EMBLEM)
    ITALY = Image.open("card_generator/assets/nation-emblems/Italy-sm.png").resize(Resizing.NATION_EMBLEM)
    JAPAN = Image.open("card_generator/assets/nation-emblems/Japan-sm.png").resize(Resizing.NATION_EMBLEM)
    US = Image.open("card_generator/assets/nation-emblems/United States-sm.png").resize(Resizing.NATION_EMBLEM)
    UK = Image.open("card_generator/assets/nation-emblems/United Kingdom-sm.png").resize(Resizing.NATION_EMBLEM)
    CANADA = Image.open("card_generator/assets/nation-emblems/Canada-sm.png").resize(Resizing.NATION_EMBLEM)
    AUSTRALIA = Image.open("card_generator/assets/nation-emblems/Australia-sm.png").resize(Resizing.NATION_EMBLEM)
    FRANCE = Image.open("card_generator/assets/nation-emblems/France-sm.png").resize(Resizing.NATION_EMBLEM)
    GREECE = Image.open("card_generator/assets/nation-emblems/Greece-sm.png").resize(Resizing.NATION_EMBLEM)
    NETHERLANDS = Image.open("card_generator/assets/nation-emblems/Netherlands-sm.png").resize(Resizing.NATION_EMBLEM)
    SWEDEN = Image.open("card_generator/assets/nation-emblems/Sweden-sm.png").resize(Resizing.NATION_EMBLEM)
    USSR = Image.open("card_generator/assets/nation-emblems/Soviet Union-sm.png").resize(Resizing.NATION_EMBLEM)
    FINLAND = Image.open("card_generator/assets/nation-emblems/Finland-sm.png").resize(Resizing.NATION_EMBLEM)
    NEW_ZEALAND = Image.open("card_generator/assets/nation-emblems/New Zealand-sm.png").resize(Resizing.NATION_EMBLEM)

    NATION_MAPPING = {
        "Australia": AUSTRALIA,
        "United States": US,
        "Canada": CANADA,
        "United Kingdom": UK,
        "Soviet Union": USSR,
        "France": FRANCE,
        "Germany": GERMANY,
        "Italy": ITALY,
        "Japan": JAPAN
    }


class Colors:
    TRANSPARENT = (255, 255, 255, 0)
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    DARK_GREY = (119, 119, 119)
    LIGHT_GREY = (137, 140, 141)
    SHIP_NAME = WHITE
    POINT_VALUE = WHITE
    SHIP_TYPE_AND_YEAR = (134, 135, 137)
    STATS = WHITE
    ATTACK_VALUE_BACKGROUND = (0, 255, 0, 80)  # transparent green


class Fonts:
    SHIP_NAME = ImageFont.truetype("card_generator/assets/Komet - Flicker - B52-Regular.ttf", 60)
    POINT_VALUE = ImageFont.truetype("card_generator/assets/Komet - Flicker - B52-Regular.ttf", 94)
    FLAGSHIP = ImageFont.truetype("card_generator/assets/RobotoSlab-Bold.ttf", 17)
    SHIP_TYPE_AND_YEAR = ImageFont.truetype("card_generator/assets/Komet - Flicker - B52-Regular.ttf", 30)
    SHIP_SPEED = ImageFont.truetype("card_generator/assets/Komet - Flicker - B52-Regular.ttf", 35)
    ATTACK_ARMOR_STATS_HEADINGS = ImageFont.truetype("card_generator/assets/Komet - Flicker - B52-Regular.ttf", 30)
    ATTACK_STATS = ImageFont.truetype("card_generator/assets/Komet - Flicker - B52-Regular.ttf", 70)
    ARMOR_STATS = ImageFont.truetype("card_generator/assets/Komet - Flicker - B52-Regular.ttf", 50)
    ABILITIES = ImageFont.truetype("card_generator/assets/RobotoSlab-Regular.ttf", 25)
    ABILITIES_TITLE = ImageFont.truetype("card_generator/assets/RobotoSlab-Bold.ttf", 25)
    SET_INFO = ImageFont.truetype("card_generator/assets/Komet - Flicker - B52-Regular.ttf", 35)


class Coordinates:
    """
    Coordinates for element placement.
    """
    NATION_EMBLEM = (44, 164)
    FLAGSHIP = (330, 206)
    POINT_CIRCLE_CENTER = (646, 125)
    SHIP_TYPE = (128, 165)
    SHIP_YEAR = (510, 165)
    SHIP_SPEED = (130, 206)

    ATTACK_HEADING = center_text(
        Values.LEFT_CARD_BORDER, 247, Values.ATTACK_RECTANGLE_START_X, 292,
        "Attacks",
        Fonts.ATTACK_ARMOR_STATS_HEADINGS
    )
    ATTACK_RANGE_HEADING_0 = (x_center_text(Values.ATTACK_RECTANGLE_START_X,
                                            Values.ATTACK_RECTANGLE_START_X + Values.DIVIDER_SPACING,
                                            "0",
                                            Fonts.ATTACK_ARMOR_STATS_HEADINGS),
                              ATTACK_HEADING[1])
    ATTACK_RANGE_HEADING_1 = (x_center_text(Values.ATTACK_RECTANGLE_START_X + Values.DIVIDER_SPACING,
                                            Values.ATTACK_RECTANGLE_START_X + (2 * Values.DIVIDER_SPACING),
                                            "1",
                                            Fonts.ATTACK_ARMOR_STATS_HEADINGS),
                              ATTACK_HEADING[1])
    ATTACK_RANGE_HEADING_2 = (x_center_text(Values.ATTACK_RECTANGLE_START_X + (2 * Values.DIVIDER_SPACING),
                                            Values.ATTACK_RECTANGLE_START_X + (3 * Values.DIVIDER_SPACING),
                                            "2",
                                            Fonts.ATTACK_ARMOR_STATS_HEADINGS),
                              ATTACK_HEADING[1])
    ATTACK_RANGE_HEADING_3 = (x_center_text(Values.ATTACK_RECTANGLE_START_X + (3 * Values.DIVIDER_SPACING),
                                            Values.ATTACK_RECTANGLE_START_X + (4 * Values.DIVIDER_SPACING),
                                            "3",
                                            Fonts.ATTACK_ARMOR_STATS_HEADINGS),
                              ATTACK_HEADING[1])

    ATTACK_HEADING_DIVIDER = [(Values.ATTACK_RECTANGLE_START_X, 254), (Values.ATTACK_RECTANGLE_START_X, 292)]
    ATTACK_HEADING_DIVIDER_1 = [
        (ATTACK_HEADING_DIVIDER[0][0] + Values.DIVIDER_SPACING, ATTACK_HEADING_DIVIDER[0][1]),
        (ATTACK_HEADING_DIVIDER[1][0] + Values.DIVIDER_SPACING, ATTACK_HEADING_DIVIDER[1][1])
    ]
    ATTACK_HEADING_DIVIDER_2 = [
        (ATTACK_HEADING_DIVIDER_1[0][0] + Values.DIVIDER_SPACING, ATTACK_HEADING_DIVIDER[0][1]),
        (ATTACK_HEADING_DIVIDER_1[1][0] + Values.DIVIDER_SPACING, ATTACK_HEADING_DIVIDER[1][1])
    ]
    ATTACK_HEADING_DIVIDER_3 = [
        (ATTACK_HEADING_DIVIDER_2[0][0] + Values.DIVIDER_SPACING, ATTACK_HEADING_DIVIDER[0][1]),
        (ATTACK_HEADING_DIVIDER_2[1][0] + Values.DIVIDER_SPACING, ATTACK_HEADING_DIVIDER[1][1])
    ]


def get_emblem(nation: Nation) -> Image.Image:
    return NationEmblems.NATION_MAPPING[nation.get_name()]


def get_attack_icon(attack: str) -> Image.Image:
    return Icons.ATTACK_ICONS[attack]


def get_header_font(text: str, tracking: int = 0) -> ImageFont.FreeTypeFont:
    correct = False
    font_size = 60
    max_size = Values.SHIP_NAME_END_X - Values.SHIP_NAME_START_X
    while not correct:
        font = ImageFont.truetype("card_generator/assets/Komet - Flicker - B52-Regular.ttf", font_size)
        width = font.getsize(text)[0] + ((tracking / 1000) * font_size * (len(text) - 1))
        correct = width <= max_size
        if not correct:
            font_size -= 1
            print("Default size is too large, trying {}".format(font_size))
    return ImageFont.truetype("card_generator/assets/Komet - Flicker - B52-Regular.ttf", font_size)


def get_set_icon(set_name: str):
    return Icons.SET_ICONS[set_name]


def get_rarity_icon(rarity: str):
    if rarity == "Common":
        return Icons.COMMON
    if rarity == "Uncommon":
        return Icons.UNCOMMON
    if rarity == "Rare":
        return Icons.RARE
    else:
        return None
