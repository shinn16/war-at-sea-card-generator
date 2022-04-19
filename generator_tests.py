import unittest
import json
from card_generator.models.utils import load_json
from card_generator.generator import Generator


class MyTestCase(unittest.TestCase):
    def test_something(self):
        data_file = open("War_at_Sea.json")
        data = json.load(data_file)
        axis_and_allies_deck = load_json(data)
        print(str(axis_and_allies_deck[0]))
        Generator(axis_and_allies_deck[1], axis_and_allies_deck[1].get_units()[30]).generate()
        data_file.close()


if __name__ == '__main__':
    unittest.main()
