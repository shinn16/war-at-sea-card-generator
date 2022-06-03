import unittest
import json
from card_generator.models.utils import load_json
from card_generator.generator import Generator


class MyTestCase(unittest.TestCase):
    def generate_all(self):
        data_file = open("War_at_Sea.json")
        data = json.load(data_file)
        axis_and_allies_deck = load_json(data)
        for nation in axis_and_allies_deck:
            for unit in nation.get_units():
                Generator(nation, unit).generate()
        data_file.close()

    def generate_country(self):
        country = 0
        data_file = open("War_at_Sea.json")
        data = json.load(data_file)
        axis_and_allies_deck = load_json(data)
        for unit in axis_and_allies_deck[country].get_units():
            Generator(axis_and_allies_deck[country], unit).generate()

    def generate_single(self):
        data_file = open("War_at_Sea.json")
        data = json.load(data_file)
        axis_and_allies_deck = load_json(data)
        Generator(axis_and_allies_deck[1], axis_and_allies_deck[1].get_units()[4]).generate(display=True)
        data_file.close()

if __name__ == '__main__':
    unittest.main()
