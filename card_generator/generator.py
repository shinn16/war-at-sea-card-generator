from PIL import Image, ImageDraw
from card_generator.models.definitions import Coordinates, Colors, Fonts, Values, get_emblem, Icons
from card_generator.models.alliance import Alliance
from card_generator.utils.helper_functions import center_text, x_center_text
from card_generator.models.nation import Nation
from card_generator.models.unit import Unit


class Generator:
    def __init__(self, nation: Nation, unit: Unit) -> None:
        self.nation = nation
        self.unit = unit
        if self.nation.getAlliance == Alliance.Allies:
            self.card_base = Image.open("assets/allies-card-base.png").convert("RGBA")
        else:
            self.card_base = Image.open("assets/axis-card-base.png").convert("RGBA")

    def generate(self) -> None:
        base_draw_layer = ImageDraw.Draw(self.card_base, "RGBA")
        transparent_overlay = Image.new("RGBA", self.card_base.size, Colors.TRANSPARENT)
        transparent_overlay_draw = ImageDraw.Draw(transparent_overlay)
        top_overlay = Image.new("RGBA", self.card_base.size, Colors.TRANSPARENT)
        top_overlay_draw = ImageDraw.Draw(top_overlay)

        def populate_header(template: Image.Image, draw_layer: ImageDraw.ImageDraw) -> Image.Image:
            template.paste(get_emblem(self.nation), Coordinates.NATION_EMBLEM,
                           get_emblem(self.nation))

            draw_layer.text(Coordinates.SHIP_NAME, self.unit.name,
                            font=Fonts.SHIP_NAME,
                            fill=Colors.SHIP_NAME)

            draw_layer.text(center_text(Coordinates.POINT_CIRCLE_CENTER, self.unit.points, Fonts.POINT_VALUE),
                            self.unit.points,
                            font=Fonts.POINT_VALUE,
                            fill=Colors.POINT_VALUE)

            draw_layer.text(Coordinates.SHIP_TYPE, self.unit.type,
                            font=Fonts.SHIP_TYPE_AND_YEAR,
                            fill=Colors.SHIP_TYPE_AND_YEAR)

            draw_layer.text(Coordinates.SHIP_YEAR, self.unit.year,
                            font=Fonts.SHIP_TYPE_AND_YEAR,
                            fill=Colors.SHIP_TYPE_AND_YEAR)

            draw_layer.text(Coordinates.SHIP_SPEED, "Speed - {}".format(self.unit.speed),
                            font=Fonts.SHIP_SPEED,
                            fill=Colors.STATS)

            if self.unit.flagship is not None:
                template.paste(Icons.FLAGSHIP, Coordinates.FLAGSHIP)
                draw_layer.text(
                    (x_center_text(
                        Coordinates.FLAGSHIP[0], Coordinates.FLAGSHIP[0] + Values.FLAGSHIP_CENTER_OFFSET,
                        self.unit.flagship,
                        Fonts.FLAGSHIP
                    ),
                     Values.FLAGSHIP_VALUE_Y
                    ),
                    self.unit.flagship,
                    font=Fonts.FLAGSHIP,
                    fill=Colors.BLACK
                )

            if self.unit.planes is not None:
                offset = Values.CARRIER_START_X
                for carrier in range(int(self.unit.planes)):
                    template.paste(Icons.CARRIER, (offset, Values.CARRIER_Y))
                    offset += Values.CARRIER_ICON_SPACING

            return template

        def populate_attack(template: Image.Image, draw_layer: ImageDraw.ImageDraw) -> Image.Image:
            pass

        def populate_armor(template: Image.Image, draw_layer: ImageDraw.ImageDraw) -> Image.Image:
            pass

        def populate_abilities(template: Image.Image, draw_layer: ImageDraw.ImageDraw) -> Image.Image:
            pass

        self.card_base = populate_header(self.card_base, base_draw_layer)
        out = Image.alpha_composite(transparent_overlay, top_overlay)
        out = Image.alpha_composite(self.card_base, out)
        out.show()
