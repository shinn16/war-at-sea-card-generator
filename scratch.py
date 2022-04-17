from PIL import Image, ImageDraw
from textwrap import wrap
from card_generator.definitions import Coordinates, Colors, Fonts, Values, NationEmblems, Icons, BackgroundAssets
from card_generator.utils import center_image, center_text, x_center_text, ability_sort

card_base = Image.open("assets/axis-card-base.png").convert("RGBA")
draw_layer = ImageDraw.Draw(card_base, "RGBA")
transparent_overlay = Image.new("RGBA", card_base.size, Colors.TRANSPARENT)
overlay_draw = ImageDraw.Draw(transparent_overlay)
top_overlay = Image.new("RGBA", card_base.size, Colors.TRANSPARENT)
top_overlay_draw = ImageDraw.Draw(top_overlay)

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

top_overlay.paste(Icons.FLAGSHIP, Coordinates.FLAGSHIP)
top_overlay_draw.text(
    (x_center_text(
        Coordinates.FLAGSHIP[0], Coordinates.FLAGSHIP[0] + Values.FLAGSHIP_CENTER_OFFSET,
        "1",
        Fonts.FLAGSHIP
    ),
     Values.FLAGSHIP_VALUE_Y
    ),
    "1",
    font=Fonts.FLAGSHIP,
    fill=Colors.BLACK
)

# 381 is x min 500 is max
carriers = 3
spacing = (Values.CARRIER_END_X - Values.CARRIER_START_X) - (carriers * Values.CARRIER_ICON_SPACING) + 5
offset = Values.CARRIER_START_X
for carrier in range(carriers):
    top_overlay.paste(Icons.CARRIER, (offset, 206))
    offset += Values.CARRIER_ICON_SPACING + spacing

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

attack_icons = [
    Icons.GUNNERY_1,
    Icons.GUNNERY_2,
    Icons.GUNNERY_3,
    Icons.ANTI_AIR,
    Icons.TORPEDO
]

attack_values = ["10", "5", "3", "-"]

y_offset = Values.ATTACK_RECTANGLE_START_Y
attacks = 5
for i in range(attacks):
    # attack icon and box
    overlay_draw.rectangle(
        (
            (Values.LEFT_CARD_BORDER, y_offset + 2),
            (Values.ATTACK_RECTANGLE_START_X, y_offset + Values.ATTACK_RECTANGLE_WIDTH)
        ),
        Colors.BLACK, None, 0)
    # attack icons
    top_overlay.paste(attack_icons[i], center_image(Values.LEFT_CARD_BORDER,
                                                    y_offset,
                                                    Values.ATTACK_RECTANGLE_START_X,
                                                    y_offset +
                                                    Values.ATTACK_RECTANGLE_WIDTH + 4,
                                                    attack_icons[i]
                                                    )
                      )

    # green transparent background
    overlay_draw.rectangle(
        (
            (Values.ATTACK_RECTANGLE_START_X, y_offset + 1),
            (Values.ATTACK_RECTANGLE_END_X, y_offset + Values.ATTACK_RECTANGLE_WIDTH)
        ),
        Colors.ATTACK_VALUE_BACKGROUND, None, 0)
    # attack vertical dividers
    overlay_draw.line(
        [
            (Values.ATTACK_VERTICAL_DIVIDER_1, y_offset + 1),
            (Values.ATTACK_VERTICAL_DIVIDER_1, y_offset + Values.ATTACK_RECTANGLE_WIDTH)
        ],
        Colors.BLACK, 1)
    overlay_draw.line(
        [
            (Values.ATTACK_VERTICAL_DIVIDER_2, y_offset + 1),
            (Values.ATTACK_VERTICAL_DIVIDER_2, y_offset + Values.ATTACK_RECTANGLE_WIDTH)
        ],
        Colors.BLACK, 1)
    overlay_draw.line(
        [
            (Values.ATTACK_VERTICAL_DIVIDER_3, y_offset + 1),
            (Values.ATTACK_VERTICAL_DIVIDER_3, y_offset + Values.ATTACK_RECTANGLE_WIDTH)
        ],
        Colors.BLACK, 1)

    # render the attacks
    for attack_range in range(4):
        # dynamically find the size of the attack value text, so it can be centered
        w, h = overlay_draw.textsize(attack_values[attack_range], font=Fonts.ATTACK_STATS)
        current_x_middle = Values.ATTACK_RECTANGLE_START_X + (Values.DIVIDER_SPACING / 2) \
                           + (attack_range * Values.DIVIDER_SPACING)
        current_y_middle = y_offset - 5 + (Values.ATTACK_RECTANGLE_WIDTH / 2)

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
                (Values.LEFT_CARD_BORDER, y_offset + 1),
                (Values.ATTACK_RECTANGLE_START_X, y_offset + 1)
            ],
            Colors.WHITE, 1)
        # black horizontal grid lines
        overlay_draw.line(
            [
                (Values.ATTACK_RECTANGLE_START_X, y_offset + 1),
                (Values.ATTACK_RECTANGLE_END_X, y_offset + 1)
            ],
            Colors.BLACK, 1)
    y_offset += Values.ATTACK_RECTANGLE_WIDTH

# black line outer border
overlay_draw.line(
    [
        (Values.ATTACK_RECTANGLE_END_X, Values.ATTACK_HEADER_Y_END),
        (Values.ATTACK_RECTANGLE_END_X, y_offset + 1)
    ],
    Colors.BLACK, Values.BORDER_WIDTH)
# white line inner border
overlay_draw.line(
    [
        (Values.ATTACK_RECTANGLE_START_X, Values.ATTACK_HEADER_Y_END),
        (Values.ATTACK_RECTANGLE_START_X, y_offset + 1)
    ],
    Colors.POINT_VALUE, Values.BORDER_WIDTH)
# bottom grey border
overlay_draw.line(
    [
        (Values.LEFT_CARD_BORDER, y_offset + 1),
        (Values.ATTACK_RECTANGLE_END_X + 1, y_offset + 1)
    ],
    Colors.LIGHT_GREY, Values.BORDER_WIDTH)

# Armor box
overlay_draw.rectangle(
    (
        (Values.LEFT_CARD_BORDER, y_offset + Values.ARMOR_ROW_TOP_MARGIN),
        (Values.LEFT_CARD_BORDER + Values.ARMOR_ROW_WIDTH,
         y_offset + Values.ARMOR_ROW_TOP_MARGIN + Values.ARMOR_ROW_HEIGHT)
    ),
    Colors.BLACK, None, 0)
# Armor box upper border
overlay_draw.line(
    [
        (Values.LEFT_CARD_BORDER, y_offset + Values.ARMOR_ROW_TOP_MARGIN),
        (Values.LEFT_CARD_BORDER + Values.ARMOR_ROW_WIDTH, y_offset + Values.ARMOR_ROW_TOP_MARGIN)
    ],
    Colors.DARK_GREY, Values.BORDER_WIDTH)

# Armor box lower border
overlay_draw.line(
    [
        (Values.LEFT_CARD_BORDER, y_offset + Values.ARMOR_ROW_TOP_MARGIN + Values.ARMOR_ROW_HEIGHT),
        (Values.LEFT_CARD_BORDER + Values.ARMOR_ROW_WIDTH,
         y_offset + Values.ARMOR_ROW_TOP_MARGIN + Values.ARMOR_ROW_HEIGHT)
    ],
    Colors.LIGHT_GREY, Values.BORDER_WIDTH)

# Armor stats headings
x_offset = Values.LEFT_CARD_BORDER

armor_values = {"ARMOR": "5", "VITAL ARMOR": "10", "HULL POINTS": "3"}
for entry in ["ARMOR", "VITAL ARMOR", "HULL POINTS"]:
    # dynamically find the size of the attack text, so it can be centered
    w, h = overlay_draw.textsize(entry, font=Fonts.ATTACK_ARMOR_STATS_HEADINGS)
    current_y_middle = y_offset + Values.ARMOR_ROW_TOP_MARGIN + (Values.ARMOR_ROW_HEIGHT / 2) - 3
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
    top_overlay.paste(BackgroundAssets.HIT_POINTS, (x_offset, y_offset + Values.ARMOR_ROW_TOP_MARGIN + 1))
    top_overlay_draw.text(
        center_text(
            x_offset,
            y_offset + Values.ARMOR_ROW_TOP_MARGIN - 6,
            x_offset + 44,
            y_offset + Values.ARMOR_ROW_TOP_MARGIN + 45,
            armor_values[entry],
            Fonts.ARMOR_STATS),
        armor_values[entry],
        font=Fonts.ARMOR_STATS,
        fill=Colors.BLACK
    )
    x_offset += 44

# ability descriptions
abilities = {"Title only ability": None, "Cool guns bro": "Whenever finger guns and takes your girl", "Dat Boi": ""
                                                                                                                 "Give "
                                                                                                                 "this "
                                                                                                                 "ship "
                                                                                                                 "the "
                                                                                                                 "ability "
                                                                                                                 "to say "
                                                                                                                 "to "
                                                                                                                 "force "
                                                                                                                 "other "
                                                                                                                 "players "
                                                                                                                 "to say "
                                                                                                                 "\"oh "
                                                                                                                 "shit, "
                                                                                                                 "its dat "
                                                                                                                 "boi\""}
y_offset += Values.ARMOR_ROW_TOP_MARGIN + 45 + Values.SPECIAL_ABILITY_TOP_MARGIN
for title, ability in sorted(abilities.items(), key=ability_sort):
    if ability is not None:
        title = title + " - "
    overlay_draw.text((Values.SPECIAL_ABILITY_LEFT_MARGIN, y_offset), title, font=Fonts.ABILITIES_TITLE,
                      fill=Colors.WHITE)
    first_line_offset = Fonts.ABILITIES_TITLE.getsize(title)[0]
    # scale the width of the first line to accommodate the title text.
    first_line_width = int(((Values.SPECIAL_ABILITY_LEFT_MARGIN + first_line_offset) / Values.ATTACK_RECTANGLE_END_X) *
                           Values.SPECIAL_ABILITY_TEXT_WIDTH)
    if ability is not None:
        text = wrap(ability, width=first_line_width)
        first_line = text[0]
        text = " ".join(text[1:])
        overlay_draw.text((Values.SPECIAL_ABILITY_LEFT_MARGIN + first_line_offset, y_offset), first_line,
                          font=Fonts.ABILITIES, fill=Colors.WHITE)
        y_offset += Fonts.ABILITIES.getsize(first_line)[1]
        for line in wrap(text, width=Values.SPECIAL_ABILITY_TEXT_WIDTH):
            overlay_draw.text((Values.SPECIAL_ABILITY_LEFT_MARGIN, y_offset), line,
                              font=Fonts.ABILITIES, fill=Colors.WHITE)
            y_offset += Fonts.ABILITIES.getsize(line)[1]
    else:
        y_offset += Fonts.ABILITIES_TITLE.getsize(title)[1]
    y_offset += Values.SPECIAL_ABILITY_BOTTOM_MARGIN

# set information
set = "set"
number = "11/42"
rarity = "o"

set_offset = 10
draw_layer.text((Values.LEFT_CARD_BORDER + set_offset, Values.SET_Y_OFFSET), set,
                font=Fonts.SET_INFO, fill=Colors.WHITE)
set_offset += Values.LEFT_CARD_BORDER + Fonts.SET_INFO.getsize(set)[0] + 10
draw_layer.text((set_offset + 10, Values.SET_Y_OFFSET), number, font=Fonts.SET_INFO, fill=Colors.WHITE)
set_offset += Fonts.SET_INFO.getsize(number)[0] + 35
draw_layer.text((set_offset, Values.SET_Y_OFFSET), rarity, font=Fonts.SET_INFO, fill=Colors.WHITE)

out = Image.alpha_composite(transparent_overlay, top_overlay)
out = Image.alpha_composite(card_base, out)

out.show()
# out.save("out.png")
