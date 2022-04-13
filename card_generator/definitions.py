from PIL import Image, ImageFont, ImageDraw
DUMMY_IMAGE = Image.new("RGBA", (739, 1045), "white")


def get_x_center(x1, x2):
    return (x1 + x2)/2


def get_x_center_text(x1, x2, text, font):
    x = get_x_center(x1, x2)
    w, h = ImageDraw.Draw(DUMMY_IMAGE).textsize(text=text, font=font)
    return x - (w/2)


def get_center(x1, y1, x2, y2):
    return (x1 + x2)/2, (y1 + y2)/2


def get_center_text(x1, y1, x2, y2, text, font):
    w, h = ImageDraw.Draw(DUMMY_IMAGE).textsize(text=text, font=font)
    x, y = get_center(x1, y1, x2, y2)
    return (x - (w/2)), (y - (h/2))


def center_text(center_point, text, font):
    w, h = ImageDraw.Draw(DUMMY_IMAGE).textsize(text=text, font=font)
    return (center_point[0] - (w / 2)), (center_point[1] - (h / 2))


class Values:
    # card positions
    LEFT_CARD_BORDER = 56

    # specific elements
    ATTACK_HEADER_Y_END = 296

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
    ARMOR_TEXT_LEFT_MARGIN = 7
    ARMOR_TEXT_RIGHT_MARGIN = 5

    BORDER_WIDTH = 3


class BackgroundAssets:
    HITPOINTS = Image.open("assets/hitpoints.png").resize((44, 44))


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
    DARK_GREY = (119, 119, 119)
    LIGHT_GREY = (137, 140, 141)
    SHIP_NAME = WHITE
    POINT_VALUE = WHITE
    SHIP_TYPE_AND_YEAR = (134, 135, 137)
    STATS = WHITE
    ATTACK_VALUE_BACKGROUND = (0, 255, 0, 80)  # transparent green


class Fonts:
    SHIP_NAME = ImageFont.truetype("assets/Komet - Flicker - B52-Regular.ttf", 75)
    POINT_VALUE = ImageFont.truetype("assets/Komet - Flicker - B52-Regular.ttf", 94)
    SHIP_TYPE_AND_YEAR = ImageFont.truetype("assets/Komet - Flicker - B52-Regular.ttf", 30)
    SHIP_SPEED = ImageFont.truetype("assets/Komet - Flicker - B52-Regular.ttf", 35)
    ATTACK_ARMOR_STATS_HEADINGS = ImageFont.truetype("assets/Komet - Flicker - B52-Regular.ttf", 30)
    ATTACK_STATS = ImageFont.truetype("assets/Komet - Flicker - B52-Regular.ttf", 70)
    ARMOR_STATS = ImageFont.truetype("assets/Komet - Flicker - B52-Regular.ttf", 50)


class Coordinates:
    NATION_EMBLEM = (45, 165)
    SHIP_NAME = (78, 91)
    POINT_CIRCLE_CENTER = (646, 125)
    SHIP_TYPE = (128, 165)
    SHIP_YEAR = (510, 165)
    SHIP_SPEED = (130, 206)

    ATTACK_HEADING = get_center_text(
        Values.LEFT_CARD_BORDER, 247, Values.ATTACK_RECTANGLE_START_X, 292,
        "Attacks",
        Fonts.ATTACK_ARMOR_STATS_HEADINGS
    )
    ATTACK_RANGE_HEADING_0 = (get_x_center_text(Values.ATTACK_RECTANGLE_START_X,
                                                Values.ATTACK_RECTANGLE_START_X + Values.DIVIDER_SPACING,
                                                "0",
                                                Fonts.ATTACK_ARMOR_STATS_HEADINGS),
                              ATTACK_HEADING[1])
    ATTACK_RANGE_HEADING_1 = (get_x_center_text(Values.ATTACK_RECTANGLE_START_X + Values.DIVIDER_SPACING,
                                                Values.ATTACK_RECTANGLE_START_X + (2 * Values.DIVIDER_SPACING),
                                                "1",
                                                Fonts.ATTACK_ARMOR_STATS_HEADINGS),
                              ATTACK_HEADING[1])
    ATTACK_RANGE_HEADING_2 = (get_x_center_text(Values.ATTACK_RECTANGLE_START_X + (2 * Values.DIVIDER_SPACING),
                                                Values.ATTACK_RECTANGLE_START_X + (3 * Values.DIVIDER_SPACING),
                                                "2",
                                                Fonts.ATTACK_ARMOR_STATS_HEADINGS),
                              ATTACK_HEADING[1])
    ATTACK_RANGE_HEADING_3 = (get_x_center_text(Values.ATTACK_RECTANGLE_START_X + (3 * Values.DIVIDER_SPACING),
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
