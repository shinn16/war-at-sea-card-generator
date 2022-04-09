from PIL import Image, ImageDraw, ImageFont
from card_generator.generator import Coordinates, Resizing, TextColor, TextSize

card_base = Image.open("assets/axis-card-base.png")
draw_layer = ImageDraw.Draw(card_base)


nameFont = ImageFont.truetype("assets/Komet - Flicker - B52-Regular.ttf", TextSize.SHIP_NAME.value)
draw_layer.text(Coordinates.SHIP_NAME.value, "T27",
                font=nameFont,
                fill=TextColor.SHIP_NAME.value)

pointFont = ImageFont.truetype("assets/Komet - Flicker - B52-Regular.ttf", TextSize.POINT_VALUE.value)
draw_layer.text(Coordinates.SINGLE_DIGIT_POINT_VALUE.value, "7",
                font=pointFont,
                fill=TextColor.POINT_VALUE.value)

shipTypeFont = ImageFont.truetype("assets/Komet - Flicker - B52-Regular.ttf", TextSize.SHIP_TYPE_AND_YEAR.value)
draw_layer.text(Coordinates.SHIP_TYPE.value, "Ship - Destroyer",
                font=shipTypeFont,
                fill=TextColor.SHIP_TYPE_AND_YEAR.value)

draw_layer.text(Coordinates.SHIP_YEAR.value, "1939",
                font=shipTypeFont,
                fill=TextColor.SHIP_TYPE_AND_YEAR.value)
speedFont = ImageFont.truetype("assets/Komet - Flicker - B52-Regular.ttf", TextSize.SHIP_SPEED.value)
draw_layer.text(Coordinates.SHIP_SPEED.value, "Speed - 2",
                font=speedFont,
                fill=TextColor.STATS.value)

attackArmorFont = ImageFont.truetype("assets/Komet - Flicker - B52-Regular.ttf", TextSize.ATTACK_ARMOR_STATS.value)
draw_layer.text((70, 257), "Attacks",
                font=attackArmorFont,
                fill=TextColor.STATS.value)

draw_layer.text((235, 257), "0",
                font=attackArmorFont,
                fill=TextColor.STATS.value)

draw_layer.text((310, 257), "1",
                font=attackArmorFont,
                fill=TextColor.STATS.value)

draw_layer.text((385, 257), "2",
                font=attackArmorFont,
                fill=TextColor.STATS.value)

draw_layer.text((465, 257), "3",
                font=attackArmorFont,
                fill=TextColor.STATS.value)

draw_layer.line([(210, 254), (210, 292)], TextColor.POINT_VALUE.value, 3)
draw_layer.line([(280, 254), (280, 292)], TextColor.POINT_VALUE.value, 1)
draw_layer.line([(355, 254), (355, 292)], TextColor.POINT_VALUE.value, 1)
draw_layer.line([(435, 254), (435, 292)], TextColor.POINT_VALUE.value, 1)

# Dynamic stuff
# draw_layer.rectangle([(65, 264), (210, 330)], (0, 0, 0), None, 0)
# draw_layer.rectangle([(65, 330), (210, 396)], (0, 0, 0), None, 0)
# draw_layer.rectangle([(65, 396), (210, 462)], (0, 0, 0), None, 0)
# draw_layer.rectangle([(65, 462), (210, 528)], (0, 0, 0), None, 0)

germany_icon = Image.open("assets/nation-emblems/Germany-sm.png")
germany_icon = germany_icon.resize(Resizing.NATION_EMBLEM.value)

card_base.paste(germany_icon, Coordinates.NATION_EMBLEM.value, germany_icon)
card_base.show()
