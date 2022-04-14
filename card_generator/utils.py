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


def get_x_center(x1, x2):
    return (x1 + x2)/2


def x_center_text(x1, x2, text, font):
    x = get_x_center(x1, x2)
    w, h = ImageDraw.Draw(DUMMY_IMAGE).textsize(text=text, font=font)
    return x - (w/2)


def get_center(x1, y1, x2, y2):
    return (x1 + x2)/2, (y1 + y2)/2


@dispatch(int, int, int, int, str, FreeTypeFont)
def center_text(x1, y1, x2, y2, text, font):
    w, h = ImageDraw.Draw(DUMMY_IMAGE).textsize(text=text, font=font)
    x, y = get_center(x1, y1, x2, y2)
    return (x - (w/2)), (y - (h/2))


@dispatch(tuple, str, FreeTypeFont)
def center_text(center_point, text, font):
    w, h = ImageDraw.Draw(DUMMY_IMAGE).textsize(text=text, font=font)
    return (center_point[0] - (w / 2)), (center_point[1] - (h / 2))
