import unittest

from card_generator.generator import PrintFormatter, PageFormat, CardFormat

class MyTestCase(unittest.TestCase):
    def test_page_layout(self):
        PrintFormatter.generate_print_layout(PageFormat.LETTER, CardFormat.STANDARD,
                                             "C:\\Users\\shinn\\Github\\war_at_sea_card_generator\\cards\\United States",
                                             "/Users/shinn/Desktop/prints")

if __name__ == '__main__':
    unittest.main()
