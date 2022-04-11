from PIL import Image, ImageDraw
from card_generator.definitions import Coordinates, Colors, Fonts, Values, NationEmblems, ICONS, DIVIDER_SPACING

card_base = Image.open("assets/axis-card-base.png").convert("RGBA")
draw_layer = ImageDraw.Draw(card_base, "RGBA")

card_base.paste(NationEmblems.GERMANY, Coordinates.NATION_EMBLEM, NationEmblems.GERMANY)

draw_layer.text(Coordinates.SHIP_NAME, "T27",
                font=Fonts.SHIP_NAME,
                fill=Colors.SHIP_NAME)

draw_layer.text(Coordinates.SINGLE_DIGIT_POINT_VALUE, "7",
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

draw_layer.line(Coordinates.ATTACK_HEADING_DIVIDER, Colors.STATS, 3)
draw_layer.line(Coordinates.ATTACK_HEADING_DIVIDER_1, Colors.STATS, 1)
draw_layer.line(Coordinates.ATTACK_HEADING_DIVIDER_2, Colors.POINT_VALUE, 1)
draw_layer.line(Coordinates.ATTACK_HEADING_DIVIDER_3, Colors.POINT_VALUE, 1)

# Dynamic stuff, done in its own overlay layers.
transparentEnablingOverlay = Image.new("RGBA", card_base.size, Colors.TRANSPARENT)
TopOverlay = Image.new("RGBA", card_base.size, Colors.TRANSPARENT)
overlayDraw = ImageDraw.Draw(transparentEnablingOverlay)

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
    overlayDraw.rectangle(
        (
            (Values.ATTACK_ICON_START_X, base + 2),
            (Values.ATTACK_RECTANGLE_START_X, base + Values.ATTACK_RECTANGLE_WIDTH)
        ),
        Colors.BLACK, None, 0)
    # attack icons
    current_icon = attack_icons[i]
    w, h = attack_icons[i].size
    current_icon = current_icon.resize((w * 2, h * 2))
    w, h = current_icon.size

    x = int(((Values.ATTACK_RECTANGLE_START_X + Values.ATTACK_ICON_START_X)/2 - (w/2)))
    y = int((base + i + 2))

    TopOverlay.paste(current_icon, (x, y))

    # green transparent background
    overlayDraw.rectangle(((Values.ATTACK_RECTANGLE_START_X, base + 1),
                           (Values.ATTACK_RECTANGLE_END_X, base + Values.ATTACK_RECTANGLE_WIDTH)),
                          Colors.ATTACK_VALUE_BACKGROUND, None, 0)
    # attack vertical dividers
    overlayDraw.line([(Values.ATTACK_VERTICAL_DIVIDER_1, base + 1), (Values.ATTACK_VERTICAL_DIVIDER_1, base + Values.ATTACK_RECTANGLE_WIDTH)],
                     Colors.BLACK, 1)
    overlayDraw.line([(Values.ATTACK_VERTICAL_DIVIDER_2, base + 1), (Values.ATTACK_VERTICAL_DIVIDER_2, base + Values.ATTACK_RECTANGLE_WIDTH)],
                     Colors.BLACK, 1)
    overlayDraw.line([(Values.ATTACK_VERTICAL_DIVIDER_3, base + 1), (Values.ATTACK_VERTICAL_DIVIDER_3, base + Values.ATTACK_RECTANGLE_WIDTH)],
                     Colors.BLACK, 1)

    # render the attacks
    for attack_range in range(4):
        # dynamically find the size of the attack value text, so it can be centered
        w, h = overlayDraw.textsize(attack_values[attack_range], font=Fonts.ATTACK_ARMOR_STATS)
        current_x_middle = Values.ATTACK_RECTANGLE_START_X + (DIVIDER_SPACING/2) + (attack_range * DIVIDER_SPACING)
        current_y_middle = base - 5 + (Values.ATTACK_RECTANGLE_WIDTH/2)

        overlayDraw.text(
            (
                current_x_middle - (w/2),
                current_y_middle - (h/2)
            ),
            attack_values[attack_range],
            font=Fonts.ATTACK_ARMOR_STATS,
            fill=Colors.STATS)

    if i == 0:
        # no horizontal border needed
        pass
    else:
        # attack icon dividers
        overlayDraw.line(
            [
                (Values.ATTACK_ICON_START_X, base + 1),
                (Values.ATTACK_RECTANGLE_START_X, base + 1)
             ],
            Colors.WHITE, 1)
        # black horizontal grid lines
        overlayDraw.line(
            [
                (Values.ATTACK_RECTANGLE_START_X, base + 1),
                (Values.ATTACK_RECTANGLE_END_X, base + 1)
            ],
            Colors.BLACK, 1)
    base += Values.ATTACK_RECTANGLE_WIDTH

# black line outer border
overlayDraw.line(
    [
        (Values.ATTACK_RECTANGLE_END_X, Values.ATTACK_HEADER_Y_END),
        (Values.ATTACK_RECTANGLE_END_X, base + 1)
    ],
    Colors.BLACK, 3)
# white line inner border
overlayDraw.line(
    [
        (Values.ATTACK_RECTANGLE_START_X, Values.ATTACK_HEADER_Y_END),
        (Values.ATTACK_RECTANGLE_START_X, base + 1)
    ],
    Colors.POINT_VALUE, 3)
# bottom grey border
overlayDraw.line(
    [
        (Values.ATTACK_ICON_START_X, base + 1),
        (Values.ATTACK_RECTANGLE_END_X + 1, base + 1)
    ],
    Colors.GREY, 3)

out = Image.alpha_composite(transparentEnablingOverlay, TopOverlay)
out = Image.alpha_composite(card_base, out)

out.show()
# out.save("out.png")
