"""
Utility classes and functions for working with images.
"""
from PIL import Image

from card_generator.utils import get_center_point


def icon_resize(icon: Image.Image, scale: float) -> Image.Image:
    """
    Resize an image using a scale.
    :param icon: image to resize
    :param scale: scale
    :return: The image scaled.
    """
    w, h = icon.size
    new_width = int(w * scale)
    new_height = int(h * scale)
    return icon.resize((new_width, new_height))


def center_image(x1: int, y1: int, x2: int, y2: int, image: Image.Image) -> tuple:
    """
    Centers an image given two points.
    :param x1: x1
    :param y1: y1
    :param x2: x2
    :param y2: y2
    :param image: image to center
    :return: Coordinates to place the image in order to center the image.
    """
    x, y = get_center_point(x1, y1, x2, y2)
    w, h = image.size
    return int(x - (w / 2)), int(y - (h / 2))


def expand_transparent_area(x_scale: float, y_scale: float, img: Image.Image) -> Image.Image:
    """
    Resizes an image, expanding its transparent area by the decimal specified.
    :param x_scale: scale to apply to the x-axis
    :param y_scale: scale to apply to the y-axis
    :param img: image to expand
    :return: image with expanded transparent area.
    """
    x, y = img.size
    x = int(x * x_scale)
    y = int(y * y_scale)

    final_image = Image.new("RGBA", (x, y), (255, 255, 255, 0))
    final_image.paste(img, center_image(0, 0, x, y, img))
    return final_image



