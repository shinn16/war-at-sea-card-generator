import unittest
import json
from card_generator.models.utils import load_json
from card_generator.utils.helper_functions import expand_transparent_area
from card_generator.generator import Generator
import os
from PIL import Image

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
        country = 2
        data_file = open("War_at_Sea.json")
        data = json.load(data_file)
        axis_and_allies_deck = load_json(data)
        for unit in axis_and_allies_deck[country].get_units():
            Generator(axis_and_allies_deck[country], unit).generate()

    def generate_single(self):
        data_file = open("War_at_Sea.json")
        data = json.load(data_file)
        axis_and_allies_deck = load_json(data)
        Generator(axis_and_allies_deck[1], axis_and_allies_deck[1].get_units()[22]).generate(display=True)
        data_file.close()

    def expand_transparent_area(self):
        DIR = "/Users/shinn/Github/war_at_sea_card_generator/card_generator/assets/silhouettes/planes/United States/"
        for item in os.listdir(DIR):
            current_path = os.path.join(DIR, item)
            img = Image.open(current_path)
            img = expand_transparent_area(1.15, 1.2, img)
            img.save(current_path)

    def json_to_csv(self):
        entities = list()
        entities.append("Nation,Unit,Class\n")
        data_file = open("War_at_Sea.json")
        data = json.load(data_file)
        axis_and_allies_deck = load_json(data)
        for nation in axis_and_allies_deck:
            for unit in nation.get_units():
                entities.append("{},{},{}\n".format(nation.name, unit.name, unit.ship_class))

        output = open("units.csv", "w+")
        output.writelines(entities)
        output.close()
        data_file.close()
if __name__ == '__main__':
    unittest.main()
