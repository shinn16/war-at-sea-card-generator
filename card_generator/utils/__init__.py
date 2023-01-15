"""
General utility functions
"""


def ability_sort(item: tuple) -> int:
    """
    Used to sort special ability headings. Prioritizes headings with no associated text, otherwise sorts by alphabetical
    order based on ability name.
    :param item: ability
    :return: sorting order.
    """
    code = 0
    # items with no value are ranked higher in priority
    if item[1] is None:
        code += ord(str.lower(item[0][0]))
    else:
        code += 26
        code += ord(str.lower(item[0][0]))
    return code


def get_axis_center_point(point1: int, point2: int) -> int:
    """
    Utility function for getting a midpoint along a straight line.
    :param point1: first point
    :param point2: second point
    :return: mid-point.
    """
    return int((point1 + point2) / 2)


def get_center_point(x1: int, y1: int, x2: int, y2: int) -> tuple:
    """
    Gets the center point between two coordinates.

    :param x1: first x
    :param y1: first y
    :param x2: second x
    :param y2: second y
    :return: center point between the provided coordinates.
    """
    return int((x1 + x2) / 2), int((y1 + y2) / 2)
