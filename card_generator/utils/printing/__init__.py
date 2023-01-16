"""Card printing utilities"""
import logging
import math
import os
import queue
from collections import deque
from enum import Enum
from queue import Queue

from PIL import Image

from card_generator import Colors

logger = logging.getLogger(__name__)


class Card:
    def __init__(self, path_for_front: str, has_back: bool, card_format: 'CardFormat', ppi: int):
        """
        Class representing the front and back of a card.
        :param path_for_front:
        :param has_back:
        """
        self.front_path = path_for_front
        if has_back:
            self.back_path = path_for_front.replace(".png", "-back.png")
        else:
            self.back_path = None
        self.card_format = card_format
        self.ppi = ppi
        if path_for_front is None:
            self.name = "Blank"
        else:
            self.name = os.path.basename(path_for_front)

    def get_front(self) -> Image.Image:
        """
        Gets the image for the front of the card, formatted for printing.
        :return: the card image.
        """
        if self.front_path is not None:
            logger.debug(f"getting {self.front_path}")
            return Image.open(self.front_path).resize(
                (self.card_format.width_in_pixels(self.ppi), self.card_format.height_in_pixels(self.ppi))
            )
        logger.debug("getting blank image")
        return self._get_blank_face()

    def get_back(self) -> Image.Image:
        """
        Gets the image for the back of the card, rotated and formatted for printing.
        :return: the image if one exists, otherwise a white image that is the same size.
        """
        if self.back_path is not None:
            logger.debug(f"getting {self.back_path}")
            back = Image.open(self.back_path)
            back = back.rotate(-90, expand=True)  # rotate the image clockwise, placing the name on the right side.
            return back.resize(
                (self.card_format.width_in_pixels(self.ppi), self.card_format.height_in_pixels(self.ppi))
            )
        logger.debug("getting blank image")
        return self._get_blank_face()

    def _get_blank_face(self):
        """
        Renders a blank card.
        :return: A plain white card.
        """
        return Image.new("RGB", self.card_format.size(self.ppi), color=Colors.WHITE)

    @staticmethod
    def get_blank_card(card_format: 'CardFormat', ppi: int):
        """
        Creates a blank card.
        :param card_format: Card format to use
        :param ppi: ppi to use
        :return: a card with blank faces.
        """
        return Card(None, False, card_format, ppi)

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.__str__()


class PageFormat(str, Enum):
    """
    Standard page formats.
    """
    width: float
    height: float

    def __new__(cls, width: float, height: float):
        obj = str.__new__(cls)
        obj._value_ = (width, height)
        obj.width = width
        obj.height = height
        return obj

    def height_in_pixels(self, ppi: int) -> int:
        return int(self.height * ppi)

    def width_in_pixels(self, ppi: int) -> int:
        return int(self.width * ppi)

    LETTER = 8.5, 11.0,
    A4 = 8.3, 11.7,
    LEGAL = 8.5, 14.0


class CardFormat(str, Enum):
    """
    Standard War At Sea card format.
    """
    width: float
    height: float

    def __new__(cls, width: float, height: float):
        """
        :param width: card width in inches.
        :param height: card height in inches.
        """
        obj = str.__new__(cls)
        obj._value_ = (width, height)
        obj.width = width
        obj.height = height
        return obj

    def size(self, ppi: int) -> tuple[int, int]:
        """
        Gets the size of the card in pixels.
        :return:
        """
        return self.width_in_pixels(ppi), self.height_in_pixels(ppi)

    def height_in_pixels(self, ppi: int) -> int:
        return int(self.height * ppi)

    def width_in_pixels(self, ppi: int) -> int:
        return int(self.width * ppi)

    STANDARD = 2.5, 3.5


class PrintFormatter:
    """
    Creates a formatted sheet of cards for printing.
    """

    @staticmethod
    def generate_print_layout(page_format: PageFormat,
                              card_format: CardFormat,
                              card_folder: str,
                              output_folder: str,
                              ppi: int = 300,
                              spacing: float = 0.05) -> None:
        """
        Generates a page of cards from a given folder. The size of the cards and size of the page are configurable based
        on the available values from PageFormat and CardFormat classes.

        :param page_format: page format to be used for printing.
        :param card_format: card format to be used for printing.
        :param card_folder: source folder for the card images.
        :param output_folder: folder to place the formatted prints.
        :param ppi: ppi to be used for printing.
        :param spacing: The spacing between cards on all sides in inches.
        """
        logger.info(f"Preparing to print on {page_format.name.lower()} page format with {card_format.name.lower()}"
                    f" card format")
        card_backs = set()
        cards = Queue()
        for card in sorted(os.listdir(card_folder)):
            logger.debug(f"Found card {card}")
            if card.endswith("-back.png"):
                card_backs.add(card)
                logger.debug(f"Adding card back {card}")
            else:
                has_back = card.replace(".png", "-back.png") in card_backs
                logger.debug(f"Checking back for {card} => {has_back}")
                card = os.path.join(card_folder, card)
                cards.put(Card(card, has_back, card_format, ppi))

        cards_per_row = int(page_format.width / card_format.width)
        cards_per_column = int(page_format.height / card_format.height)
        cards_per_page = cards_per_row * cards_per_column
        row_width = (cards_per_row * card_format.width_in_pixels(ppi)) + ((cards_per_row - 1) * spacing * ppi)
        column_height = card_format.height_in_pixels(ppi)
        number_of_pages = int(math.ceil(cards.qsize() / cards_per_page))

        logger.info("Page fits {} cards".format(cards_per_page))
        logger.debug("Cards per row: {}".format(cards_per_row))
        logger.debug("Cards per column: {}".format(cards_per_column))
        logger.debug(f"Number of cards: {cards.qsize()}")
        logger.info("Will need to print {} pages front and back to print all cards".format(number_of_pages))

        for page_number in range(number_of_pages):
            page_number += 1
            cards_queue_list = [deque() for _ in range(cards_per_row)]
            for i in range(2):  # even is front page odd is back page.
                is_front = i % 2 == 0
                if is_front:
                    output_page_path = f"{output_folder}/page-{page_number}.png"
                else:
                    output_page_path = f"{output_folder}/page-{page_number}-back.png"
                logger.debug(f"Generating {output_page_path}")
                page = Image.new("RGB", (int(page_format.width * ppi), int(page_format.height * ppi)), Colors.WHITE)
                start_x = int((page.width - row_width) / 2)
                start_y = int(
                    (page.height - ((column_height * cards_per_column) + ((cards_per_row - 1) * ppi * spacing))) / 2)
                logger.debug(f"Starting coordinate ({start_x}, {start_y})")
                for row in range(cards_per_row):
                    out_of_cards = False
                    current_x = start_x
                    current_y = start_y + (column_height * row) + int(spacing * ppi * row)
                    for column in range(cards_per_column):
                        logger.debug(f"Current row, column: {row},{column}")
                        try:
                            if is_front:
                                # if we are using the fronts, put the card back in the queue for getting the back later
                                card = cards.get(False)
                                logger.debug(f"Adding {card} to deque {row}")
                                cards_queue_list[row].append(card)
                                logger.debug(f"Adding {card} to page {page_number}.")
                                card_image = card.get_front()
                            else:
                                # if we are getting the backs, drain the queue.
                                card = cards_queue_list[row].pop()
                                logger.debug(f"Popping {card} from deque {row}")
                                logger.debug(f"Adding {card} to page {page_number}-back")
                                card_image = card.get_back()
                            logger.debug(f"Current coordinate ({current_x}, {current_y})")
                            page.paste(card_image, (current_x, current_y))
                        except (queue.Empty, IndexError):  # either of these exceptions are expected and healthy.
                            logger.info("Out of cards to add to this page")
                            if is_front:
                                # determine if we need to add blank cards to the queue to make up for empty columns.
                                remaining_row_space = cards_per_row - column
                                if remaining_row_space != 0:
                                    logger.debug(f"Row space remaining in last row, "
                                                 f"adding {remaining_row_space} blank cards")
                                    for space in range(remaining_row_space):
                                        cards_queue_list[row].append(Card.get_blank_card(card_format, ppi))
                            out_of_cards = True
                            break
                        current_x += card_format.width_in_pixels(ppi) + int(spacing * ppi)
                    if out_of_cards:
                        break

                if is_front:
                    logger.info(f"Saving page {page_number} to {output_page_path}")
                else:
                    logger.info(f"Saving back of page {page_number} to {output_page_path}")
                try:
                    page.save(output_page_path, "png")
                except FileNotFoundError:
                    os.makedirs(output_folder, exist_ok=True)
                    page.save(output_page_path, "png")
