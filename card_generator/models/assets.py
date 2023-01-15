"""
Contains various attributes and assets relating to fonts, card icons, and icon placement.
"""
import io
import importlib.resources as pkg_resources
from textwrap import wrap
from typing import BinaryIO
import logging

from PIL import ImageFont, Image

from card_generator.models.nation import Nation
from card_generator.models.unit import UnitType, Unit
from card_generator import assets
from card_generator.utils import ability_sort
from card_generator.utils.image import icon_resize
from card_generator.utils.text import x_center_text, center_text

RESOURCES = pkg_resources.files(assets)
logger = logging.getLogger(__name__)


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
    SHIP_NAME_FONT_TRACKING = 0

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

    DIVIDER_SPACING = int((ATTACK_RECTANGLE_END_X - ATTACK_RECTANGLE_START_X) / 4)

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

    SILHOUETTE_SECTION_HEIGHT = 97
    SILHOUETTE_X_MARGIN = 65
    SILHOUETTE_BASE_WIDTH = 380
    DROP_SHADOW_GROWTH = 150  # the true growth is only 90, but additional padding is added
    DROP_SHADOW_OFFSET = 45  # half of the true growth
    AIRCRAFT_SILHOUETTE_MAX_HEIGHT = 95

    BACK_TEXT_WIDTH = 85
    BLUEPRINT_MAX_WIDTH_BACK = 883


class Resizing:
    """
    Definitions for icon resizing.
    """
    NATION_EMBLEM = (61, 61)
    HIT_POINTS = (44, 44)
    FLAGSHIP = (33, 33)
    CARRIER = (33, 33)
    SET_ICONS = (30, 30)


class Background:
    """
    Background assets
    """
    with pkg_resources.path(assets, "hitpoints.png") as _resource:
        HIT_POINTS = Image.open(_resource).resize(Resizing.HIT_POINTS)
    with pkg_resources.path(assets, "axis-card-base.png") as _resource:
        AXIS_BASE = _resource
    with pkg_resources.path(assets, "axis-card-back.png") as _resource:
        AXIS_BACK = _resource
    with pkg_resources.path(assets, "allies-card-base.png") as _resource:
        ALLIES_BASE = _resource
    with pkg_resources.path(assets, "allies-card-back.png") as _resource:
        ALLIES_BACK = _resource

    @staticmethod
    def get_silhouette(unit_type: UnitType, nation: str, unit: str) -> Image.Image:
        if unit_type == UnitType.SHIP:
            resource = (RESOURCES / "silhouettes" / "ships" / nation / "{}.png".format(unit)).read_bytes()
        else:
            resource = (RESOURCES / "silhouettes" / "planes" / nation / "{}.png".format(unit)).read_bytes()
        resource = io.BytesIO(resource)
        return Image.open(resource).convert("RGBA")

    @staticmethod
    def get_blueprint(unit_type: UnitType, nation: str, unit: str) -> Image.Image:
        if unit_type == UnitType.SHIP:
            resource = (RESOURCES / "silhouettes" / "ships" / nation / "{} blueprint.png".format(unit)).read_bytes()
        else:
            resource = (RESOURCES / "silhouettes" / "planes" / nation / "{} blueprint.png".format(
                unit)).read_bytes()
        resource = io.BytesIO(resource)
        return Image.open(resource).convert("RGBA")


class Icons:
    """
    Icons including attacks, sets, and rarities.
    """
    ATTACK_ICONS = {
        "aircraft_gunnery": Image.open(io.BytesIO((RESOURCES / "card-icons" / "Gunnery1-Aircraft.png").read_bytes())),
        "main_gunnery": icon_resize(
            Image.open(io.BytesIO((RESOURCES / "card-icons" / "Gunnery1-Ship.png").read_bytes())), 0.8),
        "secondary_gunnery": icon_resize(
            Image.open(io.BytesIO((RESOURCES / "card-icons" / "Gunnery2.png").read_bytes())), 0.7),
        "tertiary_gunnery": icon_resize(
            Image.open(io.BytesIO((RESOURCES / "card-icons" / "Gunnery3.png").read_bytes())), 0.6),
        "anti-air": Image.open(io.BytesIO((RESOURCES / "card-icons" / "Antiair.png").read_bytes())),
        "bomb": Image.open(io.BytesIO((RESOURCES / "card-icons" / "Bomb.png").read_bytes())),
        "asw": Image.open(io.BytesIO((RESOURCES / "card-icons" / "ASW.png").read_bytes())),
        "torpedo": Image.open(io.BytesIO((RESOURCES / "card-icons" / "Torpedo.png").read_bytes()))
    }

    SET_ICONS = {
        "Starter Set": Image.open(io.BytesIO((RESOURCES / "card-icons" / "Flagship.png").read_bytes()))
        .resize(Resizing.SET_ICONS),
        "War At Sea": Image.open(io.BytesIO((RESOURCES / "card-icons" / "war_at_sea.png").read_bytes()))
        .resize(Resizing.SET_ICONS),
        "Task Force": Image.open(io.BytesIO((RESOURCES / "card-icons" / "task_force.png").read_bytes()))
        .resize(Resizing.SET_ICONS),
        "Flank Speed": Image.open(io.BytesIO((RESOURCES / "card-icons" / "flank_speed.png").read_bytes()))
        .resize(Resizing.SET_ICONS),
        "Condition Zebra": Image.open(io.BytesIO((RESOURCES / "card-icons" / "condition_zebra.png").read_bytes()))
        .resize(Resizing.SET_ICONS),
        "Set V": Image.open(io.BytesIO((RESOURCES / "card-icons" / "set V.png").read_bytes()))
        .resize(Resizing.SET_ICONS),
        "Surface Action": Image.open(io.BytesIO((RESOURCES / "card-icons" / "surface_action.png").read_bytes()))
        .resize(Resizing.SET_ICONS),
        "Custom": Image.open(io.BytesIO((RESOURCES / "card-icons" / "custom.png").read_bytes()))
        .resize(Resizing.SET_ICONS)
    }

    # special icons
    CARRIER = Image.open(io.BytesIO((RESOURCES / "card-icons" / "Carrier.png").read_bytes())) \
        .resize(Resizing.CARRIER)
    FLAGSHIP = Image.open(io.BytesIO((RESOURCES / "card-icons" / "Flagship.png").read_bytes())) \
        .resize(Resizing.FLAGSHIP)

    # rarity icons
    RARE = Image.open(io.BytesIO((RESOURCES / "card-icons" / "rare.png").read_bytes())).resize((30, 30))
    UNCOMMON = Image.open(io.BytesIO((RESOURCES / "card-icons" / "uncommon.png").read_bytes())).resize((30, 30))
    COMMON = Image.open(io.BytesIO((RESOURCES / "card-icons" / "common.png").read_bytes())).resize((30, 30))

    @staticmethod
    def get_set_icon(set_name: str):
        """
        Gets the icon associated with the specified set.
        :param set_name: set to get the icon for.
        :return: the set icon.
        :raises: KeyError in the event that the set is not recognized.
        """
        return Icons.SET_ICONS[set_name]

    @staticmethod
    def get_rarity_icon(rarity: str) -> [Image.Image | None]:
        """
        Returns the icon correlating to the specified rarity.
        :param rarity: rarity, can be Common, Uncommon, or Rare.
        :return: the associated rarity icon, or None if there is not one.

        """
        if rarity == "Common":
            return Icons.COMMON
        if rarity == "Uncommon":
            return Icons.UNCOMMON
        if rarity == "Rare":
            return Icons.RARE
        return None

    @staticmethod
    def get_attack_icon(attack: str) -> Image.Image:
        """
        Gets the icon associated with the attack type.
        :param attack: attack type.
        :return: sttack icon.
        """
        return Icons.ATTACK_ICONS[attack]


class NationEmblems:
    """
    Emblems and mappings relating to the various nations.
    """
    GERMANY = Image.open(io.BytesIO((RESOURCES / "nation-emblems" / "Germany-sm.png").read_bytes())) \
        .resize(Resizing.NATION_EMBLEM)
    ITALY = Image.open(io.BytesIO((RESOURCES / "nation-emblems" / "Italy-sm.png").read_bytes())) \
        .resize(Resizing.NATION_EMBLEM)
    JAPAN = Image.open(io.BytesIO((RESOURCES / "nation-emblems" / "Japan-sm.png").read_bytes())) \
        .resize(Resizing.NATION_EMBLEM)
    US = Image.open(io.BytesIO((RESOURCES / "nation-emblems" / "United States-sm.png").read_bytes())) \
        .resize(Resizing.NATION_EMBLEM)
    UK = Image.open(io.BytesIO((RESOURCES / "nation-emblems" / "United Kingdom-sm.png").read_bytes())) \
        .resize(Resizing.NATION_EMBLEM)
    CANADA = Image.open(io.BytesIO((RESOURCES / "nation-emblems" / "Canada-sm.png").read_bytes())) \
        .resize(Resizing.NATION_EMBLEM)
    AUSTRALIA = Image.open(io.BytesIO((RESOURCES / "nation-emblems" / "Australia-sm.png").read_bytes())) \
        .resize(Resizing.NATION_EMBLEM)
    FRANCE = Image.open(io.BytesIO((RESOURCES / "nation-emblems" / "France-sm.png").read_bytes())) \
        .resize(Resizing.NATION_EMBLEM)
    GREECE = Image.open(io.BytesIO((RESOURCES / "nation-emblems" / "Greece-sm.png").read_bytes())) \
        .resize(Resizing.NATION_EMBLEM)
    NETHERLANDS = Image.open(io.BytesIO((RESOURCES / "nation-emblems" / "Netherlands-sm.png").read_bytes())) \
        .resize(Resizing.NATION_EMBLEM)
    SWEDEN = Image.open(io.BytesIO((RESOURCES / "nation-emblems" / "Sweden-sm.png").read_bytes())) \
        .resize(Resizing.NATION_EMBLEM)
    USSR = Image.open(io.BytesIO((RESOURCES / "nation-emblems" / "Soviet Union-sm.png").read_bytes())) \
        .resize(Resizing.NATION_EMBLEM)
    FINLAND = Image.open(io.BytesIO((RESOURCES / "nation-emblems" / "Finland-sm.png").read_bytes())) \
        .resize(Resizing.NATION_EMBLEM)
    NEW_ZEALAND = Image.open(io.BytesIO((RESOURCES / "nation-emblems" / "New Zealand-sm.png").read_bytes())) \
        .resize(Resizing.NATION_EMBLEM)

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

    @staticmethod
    def get_emblem(nation: Nation) -> Image.Image:
        return NationEmblems.NATION_MAPPING[nation.get_name()]


class Colors:
    """
    Colors and predefined element coloring.
    """
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
    """
    Predefined fonts for the various card text.
    """
    POINT_VALUE = ImageFont.truetype(io.BytesIO((RESOURCES / "Norfolk.otf").read_bytes()), 94)
    FLAGSHIP = ImageFont.truetype(io.BytesIO((RESOURCES / "RobotoSlab-Bold.ttf").read_bytes()), 17)
    SHIP_TYPE_AND_YEAR = ImageFont.truetype(io.BytesIO((RESOURCES / "Norfolk.otf").read_bytes()), 30)
    SHIP_SPEED = ImageFont.truetype(io.BytesIO((RESOURCES / "Norfolk.otf").read_bytes()), 35)
    ATTACK_ARMOR_STATS_HEADINGS = ImageFont.truetype(io.BytesIO((RESOURCES / "Norfolk.otf").read_bytes()), 30)
    ATTACK_STATS = ImageFont.truetype(io.BytesIO((RESOURCES / "Norfolk.otf").read_bytes()), 60)
    ARMOR_STATS = ImageFont.truetype(io.BytesIO((RESOURCES / "Norfolk.otf").read_bytes()), 50)
    SET_INFO = ImageFont.truetype(io.BytesIO((RESOURCES / "Norfolk.otf").read_bytes()), 35)
    BACK_TEXT = ImageFont.truetype(io.BytesIO((RESOURCES / "RobotoSlab-Regular.ttf").read_bytes()), 20)

    @staticmethod
    def get_abilities_font(unit: Unit, y_offset: int) -> [ImageFont.FreeTypeFont, ImageFont.FreeTypeFont, int]:
        """
        Gets the fonts for the ability text and header.

        Given that the abilities font is dynamically sized to fit the available space in the abilities section of the
        card, the font itself cannot be determined without first checking the size that will fit within the bounds of
        the section.
        :return: a tuple where index 0 is the ability text font, index 1 is the ability title font, and index 2 is the
                 font size.
        """
        correct_size = False
        font_size = 25
        # dry run until we get the right size
        while not correct_size:
            abilities = ImageFont.truetype(io.BytesIO((RESOURCES / "RobotoSlab-Regular.ttf").read_bytes()), font_size)
            abilities_title = ImageFont.truetype(io.BytesIO((RESOURCES / "RobotoSlab-Bold.ttf").read_bytes()),
                                                 font_size)
            current_y_offset = y_offset + Values.ARMOR_ROW_TOP_MARGIN + 45 + Values.SPECIAL_ABILITY_TOP_MARGIN
            for title, ability in sorted(unit.special_abilities.items(), key=ability_sort):
                if ability is not None:
                    title = title + " - "
                first_line_offset = abilities_title.getsize(title)[0]
                # scale the width of the first line to accommodate the title text.
                first_line_width = int(
                    (1.2 - ((
                                    Values.SPECIAL_ABILITY_LEFT_MARGIN + first_line_offset) / Values.ATTACK_RECTANGLE_END_X)) *
                    (Values.SPECIAL_ABILITY_TEXT_WIDTH * (25 / font_size)))
                text = ability
                if ability is not None:
                    if first_line_width > 0:
                        text = wrap(text, width=first_line_width)
                        first_line = text[0]
                        text = " ".join(text[1:])
                        current_y_offset += abilities.getsize(first_line)[1]
                    else:
                        current_y_offset += abilities.getsize(title)[1]
                    for line in wrap(text, width=int((Values.SPECIAL_ABILITY_TEXT_WIDTH * (25 / font_size)))):
                        current_y_offset += abilities.getsize(line)[1]
                else:
                    current_y_offset += abilities_title.getsize(title)[1]
                current_y_offset += Values.SPECIAL_ABILITY_BOTTOM_MARGIN
            if current_y_offset < 980:
                correct_size = True
            else:
                font_size -= 1
        return (ImageFont.truetype(io.BytesIO((RESOURCES / "RobotoSlab-Regular.ttf").read_bytes()), font_size),
                ImageFont.truetype(io.BytesIO((RESOURCES / "RobotoSlab-Bold.ttf").read_bytes()), font_size),
                font_size)

    @staticmethod
    def get_header_font(text: str, tracking: int = 0) -> ImageFont.FreeTypeFont:
        """
        Sizes the card title font appropriately.
        :param text: text to size
        :param tracking: reduces the space between the individual characters by a factor of x/1000.
        :return: appropriately sized header text.
        """
        correct = False
        font_size = 60
        max_size = Values.SHIP_NAME_END_X - Values.SHIP_NAME_START_X
        while not correct:
            font = ImageFont.truetype(io.BytesIO((RESOURCES / "Norfolk.otf").read_bytes()), font_size)
            width = font.getsize(text)[0] + ((tracking / 1000) * font_size * (len(text) - 1))
            correct = width <= max_size
            if not correct:
                font_size -= 1
                logger.debug("Default size is too large, trying {}".format(font_size))
        return ImageFont.truetype(io.BytesIO((RESOURCES / "Norfolk.otf").read_bytes()), font_size)


class Coordinates:
    """
    Coordinates for element placement.
    """
    NATION_EMBLEM = (44, 164)
    FLAGSHIP = (330, 206)
    POINT_CIRCLE_CENTER = (650, 120)
    SHIP_TYPE = (128, 160)
    SHIP_YEAR = (510, 160)
    SHIP_SPEED = (130, 200)

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

    # back side of the card placement values
    NATION_EMBLEM_BACK = (23, 159)
    SHIP_TYPE_BACK = (100, 156)
    SHIP_YEAR_BACK = (630, 156)
    _DEFAULT_BLUEPRINT_BACK = (110, 720)
    BACK_TEXT = (100, 200)

    @staticmethod
    def get_default_blueprint_back_coordinates(blueprint: Image.Image) -> [int, int]:
        """
        Get the coordinates for placing the image at the bottom of the card, default placement.
        :param blueprint: image to get coords for
        :return tuple of x, y coordinate.
        """
        w, h = blueprint.size
        print(h)
        return Coordinates._DEFAULT_BLUEPRINT_BACK[0], Coordinates._DEFAULT_BLUEPRINT_BACK[1] - h


def get_war_at_sea_json() -> BinaryIO:
    """
    Gets the built-in War At Sea data set as an open file ready for reading.
    :return: War at Sea JSON file opened for reading.
    """
    return pkg_resources.open_binary(assets, "War_at_Sea.json")
