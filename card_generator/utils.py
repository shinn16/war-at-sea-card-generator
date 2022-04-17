from PIL import Image, ImageDraw
from PIL.ImageFont import FreeTypeFont
from multipledispatch import dispatch

DUMMY_IMAGE = Image.new("RGBA", (739, 1045), "white")


def ability_sort(item: tuple):
    code = 0
    # items with no value are ranked higher in priority
    if item[1] is None:
        code += ord(str.lower(item[0][0]))
    else:
        code += 26
        code += ord(str.lower(item[0][0]))
    return code


def get_x_center_point(x1, x2):
    return (x1 + x2)/2


def x_center_text(x1, x2, text, font):
    x = get_x_center_point(x1, x2)
    w, h = ImageDraw.Draw(DUMMY_IMAGE).textsize(text=text, font=font)
    return x - (w/2)


def get_center_point(x1, y1, x2, y2):
    return int((x1 + x2)/2), int((y1 + y2)/2)


@dispatch(int, int, int, int, str, FreeTypeFont)
def center_text(x1, y1, x2, y2, text, font):
    w, h = ImageDraw.Draw(DUMMY_IMAGE).textsize(text=text, font=font)
    x, y = get_center_point(x1, y1, x2, y2)
    return (x - (w/2)), (y - (h/2))


@dispatch(tuple, str, FreeTypeFont)
def center_text(center_point: tuple, text: str, font: FreeTypeFont) -> tuple:
    w, h = ImageDraw.Draw(DUMMY_IMAGE).textsize(text=text, font=font)
    return (center_point[0] - (w / 2)), (center_point[1] - (h / 2))


def icon_resize(icon: Image.Image, scale: float) -> Image.Image:
    w, h = icon.size
    new_width = int(w * scale)
    new_height = int(h * scale)
    return icon.resize((new_width, new_height))


def center_image(x1: int, y1: int, x2: int, y2: int, image: Image.Image) -> tuple:
    x, y = get_center_point(x1, y1, x2, y2)
    w, h = image.size
    return int(x - (w/2)), int(y - (h/2))
