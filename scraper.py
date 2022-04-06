from time import sleep
import requests
import json
from bs4 import BeautifulSoup
from models.unit import Unit
from models.nation import NATION_LIST
from models.utils import ModelJsonEncoder

BASE_URL = "http://was.tamgc.net/"
FACTION_PARAMETER = "query.php?faction="
UNIT_PARAMETER = "unit.php?ID="


total_records = 0
for nation in NATION_LIST:
    current_record = 1
    html_text = requests.get(BASE_URL + FACTION_PARAMETER + nation.getName()).text
    nations_page = BeautifulSoup(html_text, "html.parser")
    records = int(nations_page.find(class_="first").get_text().split(" ")[0])

    print(nation.getName() + ": " + str(records))
    total_records += records

    nation_content = nations_page.find("div", {"id": "content"})
    unit_rows = nation_content.find("table").find_all("tr")[1:] # skip the header row
    for row in unit_rows:
        print("Processing record " + str(current_record) + " of " + str(records))
        columns = row.find_all("td")
        unit_id = columns[0].find_all("a")[0]["href"].split("=")[1]
        unit_html = requests.get(BASE_URL + UNIT_PARAMETER + str(unit_id)).text
        unit_page = BeautifulSoup(unit_html, "html.parser")
       
        unit_contents = unit_page.find("div", {"id": "content"}).find_all("table")

        ship_info_table = unit_contents[0]
        ship_attack_stats_table = unit_contents[1]
        ship_armor_table = unit_contents[2]
        ship_abilits = unit_contents[3]

        unit = Unit()

        # process ship info
        rows = ship_info_table.find_all("tr")
        unit_columns = rows[1].find_all("td") # first row is a picture, second is the name and points
        unit.withName(unit_columns[0].get_text())
        unit.withPointValue(int(unit_columns[1].get_text()))

        unit_columns = rows[2].find_all("td")
        unit_spans = unit_columns[1].find_all("span")
        unit.withType(unit_spans[0].get_text())
        unit.withYear(int(unit_spans[1].get_text()))

        unit_columns = rows[3].find_all("td")
        unit.withSpeed(unit_columns[0].get_text().split("-")[1].strip())

        flagshipStat = unit_columns[1].get_text()
        carrierCapacityStat = unit_columns[2].find_all("img")

        if flagshipStat != "":
            unit.withFlagShipValue(int(flagshipStat))
        
        if len(carrierCapacityStat) > 0:
            unit.withPlaneCapacity(len(carrierCapacityStat))

        # process attack stats
        rows = ship_attack_stats_table.find_all("tr")[1:]
        for row in rows:
            row = row.find_all("td")
            attackType = row[0].find_all("img")[0]["src"].split("/")[3].split(".")[0]
            attackVector = list()
            for attack in row[1:5]:
                attackVector.append(attack.get_text())

            if   attackType == "Gunnery1-Ship":
                unit.withMainGunneryAttack(attackVector)
            elif attackType == "Gunnery1-Aircraft":
                unit.withAircraftGunneryAttack(attackVector)
            elif attackType == "Gunnery2":
                unit.withSecondaryGunneryAttack(attackVector)
            elif attackType == "Gunnery3":
                unit.withTertiaryGunneryAttack(attackVector)
            elif attackType == "Antiair":
                unit.withAntiAirAttack(attackVector)
            elif attackType == "ASW":
                unit.withAntiSubmarineAttack(attackVector)
            elif attackType == "Torpedo":
                unit.withTorpedoAttack(attackVector)
            elif attackType == "Bomb":
                unit.withBombAttack(attackVector)
            else:
                print(attackType)

        # process armor and hull points
        rows = ship_armor_table.find("tr")
        columns = rows.find_all("td")
        unit.withArmor(int(columns[1].get_text()))
        unit.withVitalArmor(int(columns[3].get_text()))
        unit.withHullPoints(int(columns[5].get_text()))

        # process abilities
        rows = ship_abilits.find_all("tr")
        abilities = dict()
        title = ""
        for row in rows[:len(rows)]: # last row is not a stat but is rather the card rarity and such
            data = row.find_all("td")[0] 
            if data["class"].__contains__("alt3") and data["class"].__contains__("ability"):
                abilities[title] = data.get_text()
            elif data["class"].__contains__("alt3"):
                abilities[data.get_text()] = None
            else:
                title = data.get_text().strip("-")
        unit.withSpecialAbilities(abilities)

        set_info = rows[len(rows) - 1].find("td").get_text().split("-")
        unit.withSet(set_info[0])
        unit.withSetNumber(set_info[1])
        unit.withRarity(set_info[2])

        nation.addUnit(unit)
        current_record += 1
        sleep(2)

outputFile = open("War_at_Sea.json", "w")
outputFile.writelines(json.dumps(NATION_LIST, cls=ModelJsonEncoder, indent=4))
outputFile.close()
print("Total records: " + str(total_records))