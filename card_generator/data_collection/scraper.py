import os.path
from time import sleep
import requests
import json
import logging
from bs4 import BeautifulSoup
from card_generator.models.unit import Unit
from card_generator.models.nation import NATION_LIST, Nation
from card_generator.models.utils import ModelJsonEncoder

logger = logging.getLogger(__name__)


class TAMGCScrapper:
    BASE_URL = "http://was.tamgc.net/"
    FACTION_PARAMETER = "query.php?faction="
    UNIT_PARAMETER = "unit.php?ID="

    def scrape(self, nation_list: {Nation} = NATION_LIST, output_folder: str = os.getcwd()):
        """
        Scrapes all the units for all nations provided in the nation list. By default, the built-in nation list is used.
        :param nation_list: list of nations to scrape, by default this is the built-in :data:`NATION_LIST`.
        :param output_folder: folder to place the scrapped data, by default this is the current directory.
        """
        total_records = 0
        for nation in nation_list:
            current_record = 1
            html_text = requests.get(self.BASE_URL + self.FACTION_PARAMETER + nation.get_name()).text
            nations_page = BeautifulSoup(html_text, "html.parser")
            records = int(nations_page.find(class_="first").get_text().split(" ")[0])

            logger.info(nation.get_name() + ": " + str(records))
            total_records += records

            nation_content = nations_page.find("div", {"id": "content"})
            unit_rows = nation_content.find("table").find_all("tr")[1:]  # skip the header row
            for row in unit_rows:
                logger.info("Processing record " + str(current_record) + " of " + str(records))
                columns = row.find_all("td")
                unit_id = columns[0].find_all("a")[0]["href"].split("=")[1]
                unit_html = requests.get(self.BASE_URL + self.UNIT_PARAMETER + str(unit_id)).text
                unit_page = BeautifulSoup(unit_html, "html.parser")

                unit_contents = unit_page.find("div", {"id": "content"}).find_all("table")

                ship_info_table = unit_contents[0]
                ship_attack_stats_table = unit_contents[1]
                ship_armor_table = unit_contents[2]
                ship_abilities = unit_contents[3]

                unit = Unit()

                # process ship info
                rows = ship_info_table.find_all("tr")
                unit_columns = rows[1].find_all("td")  # first row is a picture, second is the name and points
                unit.with_name(unit_columns[0].get_text())
                unit.with_point_value(int(unit_columns[1].get_text()))

                unit_columns = rows[2].find_all("td")
                unit_spans = unit_columns[1].find_all("span")
                unit.with_type(unit_spans[0].get_text())
                unit.with_year(int(unit_spans[1].get_text()))

                unit_columns = rows[3].find_all("td")
                unit.with_speed(unit_columns[0].get_text().split("-")[1].strip())

                flagship_stat = unit_columns[1].get_text()
                carrier_capacity_stat = unit_columns[2].find_all("img")

                if flagship_stat != "":
                    unit.with_flagship_value(int(flagship_stat))

                if len(carrier_capacity_stat) > 0:
                    unit.with_plane_capacity(len(carrier_capacity_stat))

                # process attack stats
                rows = ship_attack_stats_table.find_all("tr")[1:]
                for row in rows:
                    row = row.find_all("td")
                    attack_type = row[0].find_all("img")[0]["src"].split("/")[3].split(".")[0]
                    attack_vector = list()
                    for attack in row[1:5]:
                        attack_vector.append(attack.get_text())

                    if attack_type == "Gunnery1-Ship":
                        unit.with_main_gunnery_attack(attack_vector)
                    elif attack_type == "Gunnery1-Aircraft":
                        unit.with_aircraft_gunnery_attack(attack_vector)
                    elif attack_type == "Gunnery2":
                        unit.with_secondary_gunnery_attack(attack_vector)
                    elif attack_type == "Gunnery3":
                        unit.with_tertiary_gunnery_attack(attack_vector)
                    elif attack_type == "Antiair":
                        unit.with_anti_air_attack(attack_vector)
                    elif attack_type == "ASW":
                        unit.with_anti_submarine_attack(attack_vector)
                    elif attack_type == "Torpedo":
                        unit.with_torpedo_attack(attack_vector)
                    elif attack_type == "Bomb":
                        unit.with_bomb_attack(attack_vector)

                # process armor and hull points
                rows = ship_armor_table.find("tr")
                columns = rows.find_all("td")
                unit.with_armor(int(columns[1].get_text()))
                unit.with_vital_armor(int(columns[3].get_text()))
                unit.with_hull_points(int(columns[5].get_text()))

                # process abilities
                rows = ship_abilities.find_all("tr")
                abilities = dict()
                title = ""
                for row in rows[:len(rows)]:  # last row is not a stat but is rather the card rarity and such
                    data = row.find_all("td")[0]
                    if data["class"].__contains__("alt3") and data["class"].__contains__("ability"):
                        abilities[title] = data.get_text()
                    elif data["class"].__contains__("alt3"):  # title with no ability text
                        abilities[data.contents[0].strip("-").strip(" ")] = None
                    else:
                        title = data.get_text().strip("-").strip(" ")
                unit.with_special_abilities(abilities)

                set_info = rows[len(rows) - 1].find("td").get_text().split("-")
                unit.with_set(set_info[0].strip(" "))
                unit.with_set_number(set_info[1].strip(" "))
                unit.with_rarity(set_info[2].strip(" "))

                nation.add_unit(unit)
                current_record += 1
                sleep(2)

        output_file = open(os.path.join(output_folder, "War_at_Sea.json"), "w")
        output_file.writelines(json.dumps(NATION_LIST, cls=ModelJsonEncoder, indent=4))
        output_file.close()
        logger.info("Total records: " + str(total_records))
