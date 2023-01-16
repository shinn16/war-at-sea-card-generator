import unittest

from card_generator.utils.printing import PrintFormatter, PageFormat, CardFormat, CardFace


class PrintTestCases(unittest.TestCase):
    def test_page_layout(self):
        PrintFormatter.generate_print_layout(PageFormat.LETTER, CardFormat.STANDARD,
                                             "C:\\Users\\shinn\\Github\\war_at_sea_card_generator\\cards\\Australia",
                                             "/Users/shinn/Desktop/print-test")

    def test_card_rotate(self):
        CardFace(
            "C:\\Users\\shinn\\Desktop\\cards\\Australia\\HMAS Arunta.png",
            True,
            CardFormat.STANDARD,
            300
        ).get_back().show()


if __name__ == '__main__':
    unittest.main()
