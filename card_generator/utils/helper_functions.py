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
