from PIL import Image, ImageDraw, ImageFont
from card_generator.generator import Coordinates, Resizing, TextColor, TextSize

card_base = Image.open("assets/axis-card-base.png").convert("RGBA")
draw_layer = ImageDraw.Draw(card_base, "RGBA")

germany_icon = Image.open("assets/nation-emblems/Germany-sm.png")
germany_icon = germany_icon.resize(Resizing.NATION_EMBLEM.value)

card_base.paste(germany_icon, Coordinates.NATION_EMBLEM.value, germany_icon)

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
draw_layer.text((72, 257), "Attacks",
                font=attackArmorFont,
                fill=TextColor.STATS.value)

draw_layer.text((240, 257), "0",
                font=attackArmorFont,
                fill=TextColor.STATS.value)

draw_layer.text((317, 257), "1",
                font=attackArmorFont,
                fill=TextColor.STATS.value)

draw_layer.text((391, 257), "2",
                font=attackArmorFont,
                fill=TextColor.STATS.value)

draw_layer.text((465, 257), "3",
                font=attackArmorFont,
                fill=TextColor.STATS.value)

draw_layer.line([(210, 254), (210, 292)], TextColor.POINT_VALUE.value, 3)
draw_layer.line([(286, 254), (286, 292)], TextColor.POINT_VALUE.value, 1)
draw_layer.line([(361, 254), (361, 292)], TextColor.POINT_VALUE.value, 1)
draw_layer.line([(436, 254), (436, 292)], TextColor.POINT_VALUE.value, 1)

# Dynamic stuff
transparentEnablingOverlay = Image.new("RGBA", card_base.size, (255, 255, 255, 0))
TopOverlay = Image.new("RGBA", card_base.size, (255, 255, 255, 0))
overlayDraw = ImageDraw.Draw(transparentEnablingOverlay)

attack_icons = [
    Image.open("assets/card-icons/Gunnery1-Ship.png"),
    Image.open("assets/card-icons/Gunnery2.png"),
    Image.open("assets/card-icons/Gunnery3.png"),
    Image.open("assets/card-icons/Antiair.png"),
    Image.open("assets/card-icons/Torpedo.png")
]

# 65
base = 295
width = 55
attacks = 4
for i in range(attacks):
    # attack icon and box
    overlayDraw.rectangle([(56, base + 2), (210, base + width)], (0, 0, 0), None, 0)
    # attack icons
    current_icon = attack_icons[i]
    w, h = attack_icons[i].size
    current_icon = current_icon.resize((w * 2, h * 2))
    w, h = current_icon.size
    print(type(w))
    x = int(((210+56)/2 - (w/2)))
    y = int((base + i + 1))

    print(str(w) + ", " + str(h))
    TopOverlay.paste(current_icon, (x, y))

    # green transparent background
    overlayDraw.rectangle([(210, base + 1), (513, base + width)], (0, 255, 0, 80), None, 0)
    # attack vertical dividers
    overlayDraw.line([(286, base + 1), (286, base + width)], (0, 0, 0), 1)
    overlayDraw.line([(361, base + 1), (361, base + width)], (0, 0, 0), 1)
    overlayDraw.line([(436, base + 1), (436, base + width)], (0, 0, 0), 1)
    if i == 0:
        # no horizontal border needed
        pass
    else:
        overlayDraw.line([(56, base + 1), (210,  base + 1)], TextColor.POINT_VALUE.value, 1)
        overlayDraw.line([(211, base + 1), (513, base + 1)], (0, 0, 0), 1)
    base += width

# black line outer border
overlayDraw.line([(513, 296), (513, base + 1)], (0, 0, 0), 3)
# white line inner border
overlayDraw.line([(210, 292), (210, base + 1)], TextColor.POINT_VALUE.value, 3)
# bottom grey border
overlayDraw.line([(56, base + 1), (514, base + 1)], (137, 140, 141), 3)


out = Image.alpha_composite(transparentEnablingOverlay, TopOverlay)
out = Image.alpha_composite(card_base, out)
out.show()
