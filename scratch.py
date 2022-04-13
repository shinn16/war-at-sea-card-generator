from PIL import Image, ImageDraw
from card_generator.definitions import Coordinates, Colors, Fonts, Values, \
    NationEmblems, Icons, center_text, get_center_text, BackgroundAssets

card_base = Image.open("assets/axis-card-base.png").convert("RGBA")
draw_layer = ImageDraw.Draw(card_base, "RGBA")

card_base.paste(NationEmblems.GERMANY, Coordinates.NATION_EMBLEM, NationEmblems.GERMANY)

draw_layer.text(Coordinates.SHIP_NAME, "T27",
                font=Fonts.SHIP_NAME,
                fill=Colors.SHIP_NAME)

draw_layer.text(center_text(Coordinates.POINT_CIRCLE_CENTER, "7", Fonts.POINT_VALUE),
                "7",
                font=Fonts.POINT_VALUE,
                fill=Colors.POINT_VALUE)

draw_layer.text(Coordinates.SHIP_TYPE, "Ship - Destroyer",
                font=Fonts.SHIP_TYPE_AND_YEAR,
                fill=Colors.SHIP_TYPE_AND_YEAR)

draw_layer.text(Coordinates.SHIP_YEAR, "1939",
                font=Fonts.SHIP_TYPE_AND_YEAR,
                fill=Colors.SHIP_TYPE_AND_YEAR)

draw_layer.text(Coordinates.SHIP_SPEED, "Speed - 2",
                font=Fonts.SHIP_SPEED,
                fill=Colors.STATS)

draw_layer.text(Coordinates.ATTACK_HEADING, "Attacks",
                font=Fonts.ATTACK_ARMOR_STATS_HEADINGS,
                fill=Colors.STATS)

draw_layer.text(Coordinates.ATTACK_RANGE_HEADING_0, "0",
                font=Fonts.ATTACK_ARMOR_STATS_HEADINGS,
                fill=Colors.STATS)

draw_layer.text(Coordinates.ATTACK_RANGE_HEADING_1, "1",
                font=Fonts.ATTACK_ARMOR_STATS_HEADINGS,
                fill=Colors.STATS)

draw_layer.text(Coordinates.ATTACK_RANGE_HEADING_2, "2",
                font=Fonts.ATTACK_ARMOR_STATS_HEADINGS,
                fill=Colors.STATS)

draw_layer.text(Coordinates.ATTACK_RANGE_HEADING_3, "3",
                font=Fonts.ATTACK_ARMOR_STATS_HEADINGS,
                fill=Colors.STATS)

draw_layer.line(Coordinates.ATTACK_HEADING_DIVIDER, Colors.STATS, Values.BORDER_WIDTH)
draw_layer.line(Coordinates.ATTACK_HEADING_DIVIDER_1, Colors.STATS, 1)
draw_layer.line(Coordinates.ATTACK_HEADING_DIVIDER_2, Colors.POINT_VALUE, 1)
draw_layer.line(Coordinates.ATTACK_HEADING_DIVIDER_3, Colors.POINT_VALUE, 1)

# Dynamic stuff, done in its own overlay layers.
transparent_overlay = Image.new("RGBA", card_base.size, Colors.TRANSPARENT)
top_overlay = Image.new("RGBA", card_base.size, Colors.TRANSPARENT)
top_overlay_draw = ImageDraw.Draw(top_overlay)
overlay_draw = ImageDraw.Draw(transparent_overlay)

attack_icons = [
    Image.open("assets/card-icons/Gunnery1-Ship.png"),
    Image.open("assets/card-icons/Gunnery2.png"),
    Image.open("assets/card-icons/Gunnery3.png"),
    Image.open("assets/card-icons/Antiair.png"),
    Image.open("assets/card-icons/Torpedo.png")
]

attack_values = ["10", "5", "3", "-"]

base = Values.ATTACK_RECTANGLE_START_Y
attacks = 5
for i in range(attacks):
    # attack icon and box
    overlay_draw.rectangle(
        (
            (Values.LEFT_CARD_BORDER, base + 2),
            (Values.ATTACK_RECTANGLE_START_X, base + Values.ATTACK_RECTANGLE_WIDTH)
        ),
        Colors.BLACK, None, 0)
    # attack icons
    current_icon = attack_icons[i]
    w, h = attack_icons[i].size
    current_icon = current_icon.resize((w * 2, h * 2))
    w, h = current_icon.size

    x = int(((Values.ATTACK_RECTANGLE_START_X + Values.LEFT_CARD_BORDER) / 2 - (w / 2)))
    y = int((base + i + 2))

    top_overlay.paste(current_icon, (x, y))

    # green transparent background
    overlay_draw.rectangle(
        (
            (Values.ATTACK_RECTANGLE_START_X, base + 1),
            (Values.ATTACK_RECTANGLE_END_X, base + Values.ATTACK_RECTANGLE_WIDTH)
        ),
        Colors.ATTACK_VALUE_BACKGROUND, None, 0)
    # attack vertical dividers
    overlay_draw.line(
        [
            (Values.ATTACK_VERTICAL_DIVIDER_1, base + 1),
            (Values.ATTACK_VERTICAL_DIVIDER_1, base + Values.ATTACK_RECTANGLE_WIDTH)
        ],
        Colors.BLACK, 1)
    overlay_draw.line(
        [
            (Values.ATTACK_VERTICAL_DIVIDER_2, base + 1),
            (Values.ATTACK_VERTICAL_DIVIDER_2, base + Values.ATTACK_RECTANGLE_WIDTH)
        ],
        Colors.BLACK, 1)
    overlay_draw.line(
        [
            (Values.ATTACK_VERTICAL_DIVIDER_3, base + 1),
            (Values.ATTACK_VERTICAL_DIVIDER_3, base + Values.ATTACK_RECTANGLE_WIDTH)
        ],
        Colors.BLACK, 1)

    # render the attacks
    for attack_range in range(4):
        # dynamically find the size of the attack value text, so it can be centered
        w, h = overlay_draw.textsize(attack_values[attack_range], font=Fonts.ATTACK_STATS)
        current_x_middle = Values.ATTACK_RECTANGLE_START_X + (Values.DIVIDER_SPACING / 2) \
                           + (attack_range * Values.DIVIDER_SPACING)
        current_y_middle = base - 5 + (Values.ATTACK_RECTANGLE_WIDTH / 2)

        overlay_draw.text(
            (
                current_x_middle - (w / 2),
                current_y_middle - (h / 2)
            ),
            attack_values[attack_range],
            font=Fonts.ATTACK_STATS,
            fill=Colors.STATS)

    if i == 0:
        # no horizontal border needed
        pass
    else:
        # attack icon dividers
        overlay_draw.line(
            [
                (Values.LEFT_CARD_BORDER, base + 1),
                (Values.ATTACK_RECTANGLE_START_X, base + 1)
            ],
            Colors.WHITE, 1)
        # black horizontal grid lines
        overlay_draw.line(
            [
                (Values.ATTACK_RECTANGLE_START_X, base + 1),
                (Values.ATTACK_RECTANGLE_END_X, base + 1)
            ],
            Colors.BLACK, 1)
    base += Values.ATTACK_RECTANGLE_WIDTH

# black line outer border
overlay_draw.line(
    [
        (Values.ATTACK_RECTANGLE_END_X, Values.ATTACK_HEADER_Y_END),
        (Values.ATTACK_RECTANGLE_END_X, base + 1)
    ],
    Colors.BLACK, Values.BORDER_WIDTH)
# white line inner border
overlay_draw.line(
    [
        (Values.ATTACK_RECTANGLE_START_X, Values.ATTACK_HEADER_Y_END),
        (Values.ATTACK_RECTANGLE_START_X, base + 1)
    ],
    Colors.POINT_VALUE, Values.BORDER_WIDTH)
# bottom grey border
overlay_draw.line(
    [
        (Values.LEFT_CARD_BORDER, base + 1),
        (Values.ATTACK_RECTANGLE_END_X + 1, base + 1)
    ],
    Colors.LIGHT_GREY, Values.BORDER_WIDTH)

# Armor box
overlay_draw.rectangle(
    (
        (Values.LEFT_CARD_BORDER, base + Values.ARMOR_ROW_TOP_MARGIN),
        (Values.LEFT_CARD_BORDER + Values.ARMOR_ROW_WIDTH, base + Values.ARMOR_ROW_TOP_MARGIN + Values.ARMOR_ROW_HEIGHT)
    ),
    Colors.BLACK, None, 0)
# Armor box upper border
overlay_draw.line(
    [
        (Values.LEFT_CARD_BORDER, base + Values.ARMOR_ROW_TOP_MARGIN),
        (Values.LEFT_CARD_BORDER + Values.ARMOR_ROW_WIDTH, base + Values.ARMOR_ROW_TOP_MARGIN)
    ],
    Colors.DARK_GREY, Values.BORDER_WIDTH)

# Armor box lower border
overlay_draw.line(
    [
        (Values.LEFT_CARD_BORDER, base + Values.ARMOR_ROW_TOP_MARGIN + Values.ARMOR_ROW_HEIGHT),
        (Values.LEFT_CARD_BORDER + Values.ARMOR_ROW_WIDTH, base + Values.ARMOR_ROW_TOP_MARGIN + Values.ARMOR_ROW_HEIGHT)
    ],
    Colors.LIGHT_GREY, Values.BORDER_WIDTH)

# Armor stats headings
x_offset = Values.LEFT_CARD_BORDER

armor_values = {"ARMOR": "5", "VITAL ARMOR": "10", "HULL POINTS": "3"}
for entry in ["ARMOR", "VITAL ARMOR", "HULL POINTS"]:
    # dynamically find the size of the attack text, so it can be centered
    w, h = overlay_draw.textsize(entry, font=Fonts.ATTACK_ARMOR_STATS_HEADINGS)
    current_y_middle = base + Values.ARMOR_ROW_TOP_MARGIN + (Values.ARMOR_ROW_HEIGHT / 2) - 3
    overlay_draw.text(
        (
            x_offset + Values.ARMOR_TEXT_LEFT_MARGIN,
            current_y_middle - (h / 2)
        ),
        entry,
        font=Fonts.ATTACK_ARMOR_STATS_HEADINGS,
        fill=Colors.STATS)
    x_offset += w + Values.ARMOR_TEXT_LEFT_MARGIN + Values.ARMOR_TEXT_RIGHT_MARGIN
    # Add a box for the values
    top_overlay.paste(BackgroundAssets.HITPOINTS, (x_offset,  base + Values.ARMOR_ROW_TOP_MARGIN + 1))
    top_overlay_draw.text(
        get_center_text(
            x_offset, 
            base + Values.ARMOR_ROW_TOP_MARGIN -6,
            x_offset + 44,
            base + Values.ARMOR_ROW_TOP_MARGIN + 45, 
            armor_values[entry],
            Fonts.ARMOR_STATS),
        armor_values[entry],
        font=Fonts.ARMOR_STATS,
        fill=Colors.BLACK
    )
    x_offset += 44

out = Image.alpha_composite(transparent_overlay, top_overlay)
out = Image.alpha_composite(card_base, out)

out.show()
# out.save("out.png")
