from json.encoder import JSONEncoder
from card_generator.models.alliance import Alliance
from card_generator.models.nation import Nation, NATION_LIST
from card_generator.models.unit import Unit
import logging

log = logging.getLogger(__name__)


class ModelJsonEncoder(JSONEncoder):
    def default(self, o):
        if isinstance(o, Nation):
            return o.__dict__
        elif isinstance(o, Unit):
            return o.__dict__
        elif isinstance(o, Alliance):
            return o.value
        return super().default(o)


def load_json(json) -> list:
    try:
        populated_nations = list()
        for nation in json:
            current_nation = Nation(nation["name"], nation["alliance"])
            for unit in nation["units"]:
                current_unit = Unit() \
                    .with_name(unit["name"]) \
                    .with_flagship_value(unit["flagship"]) \
                    .with_point_value(unit["points"]) \
                    .with_year(unit["year"]) \
                    .with_type(unit["type"]).with_speed(unit["speed"]) \
                    .with_plane_capacity(unit["planes"]) \
                    .with_main_gunnery_attack(unit["main_gunnery_attack"]) \
                    .with_secondary_gunnery_attack(unit["secondary_gunnery_attack"]) \
                    .with_tertiary_gunnery_attack(unit["tertiary_gunnery_attack"]) \
                    .with_anti_air_attack(unit["anti_aircraft_attack"]) \
                    .with_anti_submarine_attack(unit["anti_submarine_attack"]) \
                    .with_torpedo_attack(unit["torpedo_attack"]) \
                    .with_bomb_attack(unit["bomb_attack"]) \
                    .with_armor(unit["armor"]) \
                    .with_vital_armor(unit["vital_armor"]) \
                    .with_hull_points(unit["hull_points"]) \
                    .with_special_abilities(unit["special_abilities"]) \
                    .with_set(unit["set"]) \
                    .with_set_number(unit["set_number"]) \
                    .with_rarity(unit["rarity"])
                try:
                    current_unit = current_unit.with_ship_class(unit["class"])
                except KeyError:
                    # TODO all aircraft will need their manufacturer listed.
                    # current_unit = current_unit.with_manufacturer(unit["manufacturer"])
                    pass
                try:
                    current_unit = current_unit.with_blueprint_settings(unit["blue_print_settings"])
                except KeyError:
                    current_unit = current_unit.with_blueprint_settings(dict())

                try:
                    current_unit = current_unit.with_back_text(unit["back_text"])
                except KeyError:
                    pass
                current_nation.add_unit(current_unit)
            populated_nations.append(current_nation)
        return populated_nations
    except Exception as e:
        log.error("There was an issue parsing {}\n{}: {}".format(unit, type(e), e))
        exit(1)
