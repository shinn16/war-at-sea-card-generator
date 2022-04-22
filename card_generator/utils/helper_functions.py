from PIL import Image, ImageDraw, ImageFont
from PIL.ImageFont import FreeTypeFont
from multipledispatch import dispatch


def ability_sort(item: tuple):
    code = 0
    # items with no value are ranked higher in priority
    if item[1] is None:
        code += ord(str.lower(item[0][0]))
    else:
        code += 26
        code += ord(str.lower(item[0][0]))
    return code


def get_axis_center_point(point1, point2):
    return (point1 + point2) / 2


def x_center_text(x1, x2, text, font: FreeTypeFont):
    x = get_axis_center_point(x1, x2)
    w, h = font.getsize(text)
    return x - (w / 2)


def y_center_text(y1, y2, text, font: FreeTypeFont):
    y = get_axis_center_point(y1, y2)
    w, h = font.getsize(text)
    return int(y - ((h * 1.25) / 2))


def get_center_point(x1, y1, x2, y2):
    return int((x1 + x2) / 2), int((y1 + y2) / 2)


@dispatch(int, int, int, int, str, FreeTypeFont)
def center_text(x1, y1, x2, y2, text, font: FreeTypeFont):
    w, h = font.getsize(text)
    x, y = get_center_point(x1, y1, x2, y2)
    return (x - (w / 2)), (y - (h / 2))


@dispatch(tuple, str, FreeTypeFont)
def center_text(center_point: tuple, text: str, font: FreeTypeFont) -> tuple:
    w, h = font.getsize(text)
    return (center_point[0] - (w / 2)), (center_point[1] - (h / 2))


def icon_resize(icon: Image.Image, scale: float) -> Image.Image:
    w, h = icon.size
    new_width = int(w * scale)
    new_height = int(h * scale)
    return icon.resize((new_width, new_height))


def center_image(x1: int, y1: int, x2: int, y2: int, image: Image.Image) -> tuple:
    x, y = get_center_point(x1, y1, x2, y2)
    w, h = image.size
    return int(x - (w / 2)), int(y - (h / 2))


# thanks https://stackoverflow.com/questions/49530282/python-pil-decrease-letter-spacing
def draw_text_psd_style(draw, xy, text, font, tracking=0, leading=None, **kwargs):
    """
    usage: draw_text_psd_style(draw, (0, 0), "Test",
                tracking=-0.1, leading=32, fill="Blue")

    Leading is measured from the baseline of one line of text to the
    baseline of the line above it. Baseline is the invisible line on which most
    letters—that is, those without descenders—sit. The default auto-leading
    option sets the leading at 120% of the type size (for example, 12‑point
    leading for 10‑point type).

    Tracking is measured in 1/1000 em, a unit of measure that is relative to
    the current type size. In a 6 point font, 1 em equals 6 points;
    in a 10 point font, 1 em equals 10 points. Tracking
    is strictly proportional to the current type size.
    """

    def stutter_chunk(lst, size, overlap=0, default=None):
        for i in range(0, len(lst), size - overlap):
            r = list(lst[i:i + size])
            while len(r) < size:
                r.append(default)
            yield r

    x, y = xy
    font_size = font.size
    lines = text.splitlines()
    x_offset = (tracking / 1000) * font_size * (len(text) - 1)
    if leading is None:
        leading = font.size * 1.2
    x -= x_offset/2
    for line in lines:
        for a, b in stutter_chunk(line, 2, 1, ' '):
            w = font.getlength(a + b) - font.getlength(b)
            draw.text((x, y), a, font=font, **kwargs)
            x += w + (tracking / 1000) * font_size
        y += leading
        x = xy[0]