"""
A collection of utility classes and functions that improve code readability and reliability.
"""


import logging
from typing import Tuple

import numpy as np
from PIL import Image
from PIL import ImageFont
from PIL.ImageDraw import Draw

from card_generator.models.assets import Colors

log = logging.getLogger(__name__)


class ImageTextWrap:

    def __init__(self, font: ImageFont.FreeTypeFont,
                 image: Image.Image,
                 wrap_over: list = [[0, 0, 0, 0]],
                 margin: int = 0):
        """
        Wraps text around the contents of an image, only populating the transparent areas.

        :param font: font the wrapped text will be displayed in
        :param image: image to wrap the text around
        :keyword wrap_over: pixels that text can be displayed over. Defaults to transparent.
        :keyword margin: margin around the image contents in pixels, default is 0
        :return:
        """
        self._font = font
        self._image = image
        self._pixels = np.array(image)
        self._image_width = image.size[0]
        self._image_height = image.size[1]
        self._wrap_over = wrap_over
        self._margin = margin
        self._last_x_pixel_checked = 0
        self._last_x_pixel_written = 0
        log.debug(f"Image width: {self._image_width}, height: {self._image_height}")

    @staticmethod
    def _split_last_word(buffer: str) -> Tuple[str, str]:
        """
        Splits off the last word into a new string.

        :param buffer: String buffer to process
        :return: a buffer containing the first portion of the string, an exchange buffer containing the last word.
        """
        add_space = False
        if buffer[-1] == " ":
            buffer = buffer.strip()
            add_space = True
        slice_size = 0
        for character in buffer[::-1]:  # reverse the buffer and work our way backwards to find the first space
            if character == " ":
                break
            else:
                slice_size += 1
        # extract the slice
        slice_size *= -1
        exchange_buffer = buffer[slice_size:]
        if add_space:
            exchange_buffer += " "
        # trim the buffer, keep in mind that slice size is negative at this point.
        buffer = buffer[:len(buffer) + slice_size]
        return buffer, exchange_buffer

    def _is_blank_area(self, buffer_width: int, y_offset: int, buffer_height: int, start_x: int = 0):
        """
        Checks to see if writing the current buffer will run into a non-safe pixel.
        :param buffer_width: width of the current buffer
        :param y_offset: current y offset
        :param buffer_height: height of the current buffer
        :return: True is the checked area is blank, otherwise False.
        """
        log.debug(f"Checking pixels {self._last_x_pixel_checked},{y_offset} to {buffer_width},{y_offset + buffer_height - 1}")
        for y in range(y_offset, y_offset + buffer_height - 1):
            for x in range(self._last_x_pixel_checked, buffer_width + 1):
                log.debug(f"Checking pixel at {x},{y}")
                pixel = self._pixels[y][x].tolist()
                if pixel not in self._wrap_over:
                    self._last_x_pixel_checked = start_x
                    log.debug(f"Unsafe pixel detected at {x}, {y} with value {pixel}, wrapping text")
                    return False
        log.debug(f"All pixels are safe, setting last checked x to {buffer_width}")
        self._last_x_pixel_checked = buffer_width
        return True

    def wrap_around(self, text: str,
                    start_coord: tuple[int, int] = (0, 0)) -> Image.Image:
        """
        Wraps text around the non-transparent part of an image.

        :param start_coord:
        :param text: text to wrap
        :return: Image with applied text wrapping.
        """
        base_draw = Draw(self._image, "RGBA")
        # lines to be written out
        lines = list()
        # buffers for holding words between writing
        exchange_buffer = ""
        buffer = ""
        # offset down the image to check
        y_offset = start_coord[1]
        # a place to fit the current buffer has been found
        fit_found = True
        # start a new line
        new_line = True
        for i, character in enumerate(text):
            if new_line:
                buffer = exchange_buffer
                exchange_buffer = ""
                new_line = False
            buffer += character
            buffer_width, font_height = self._font.getsize(buffer)
            buffer_width += start_coord[0]
            if y_offset + font_height >= self._image_height:
                log.warning("The rest of the text could not be wrapped.")
                break
            # if the width of the line is greater than the width of the image we are producing, break the line
            log.debug(f"checking character: {character}")
            if buffer_width >= self._image_width or \
                    not self._is_blank_area(buffer_width, y_offset, font_height, start_x=start_coord[0]):
                buffer, exchange_buffer = self._split_last_word(buffer)
                new_line = True
                if buffer == "":
                    # only one word was in the buffer, find a place to put it before continuing
                    log.debug("Single word found that may not fit, checking next line")
                    fit_found = False
                    while not fit_found:
                        y_offset += font_height
                        if y_offset + font_height >= self._image_height:
                            # we have run out of room.
                            break
                        fit_found = self._is_blank_area(buffer_width, y_offset, font_height)
                if fit_found:
                    lines.append(buffer)
                y_offset += self._font.size
            # catch the last line
            elif i == len(text) - 1:
                lines.append(buffer)
        y_offset = 0 + start_coord[1]
        for line in lines:
            base_draw.text((0 + start_coord[0], y_offset), line, font=self._font, fill=Colors.WHITE)
            y_offset += self._font.size
        return self._image
