import json
import argparse
import logging

from card_generator.generator import Generator
from card_generator.models.assets import get_war_at_sea_json
from card_generator.models.utils import load_json

logger = logging.getLogger(__name__)


def generate_all(output_folder: str = None):
    """
    Generates all units that are present in the included War at Sea data file.
    :param output_folder: folder to dump the cards to, defaults to the current directory.
    """
    data_file = get_war_at_sea_json()
    data = json.load(data_file)
    axis_and_allies_deck = load_json(data)
    for nation in axis_and_allies_deck:
        for unit in nation.get_units():
            Generator(nation, unit).generate_front(output_folder=output_folder)
    data_file.close()


def generate_country(country: str, output_folder: str = None, full: bool = False):
    """
    Generates all units for a given country.
    :param country: name of the nation to generate units for.
    :param output_folder: folder to dump the cards to, defaults to the current directory.
    :param full: whether to generate both the front and backs of the cards, defaults to false which generates only the
                 front.
    """
    data_file = get_war_at_sea_json()
    data = json.load(data_file)
    axis_and_allies_deck = load_json(data)
    try:
        index = 0
        for candidate_country in axis_and_allies_deck:
            if candidate_country.name == country:
                break
            else:
                index += 1
        if index == len(axis_and_allies_deck):
            raise ValueError("\"{}\" does not exist in the default countries".format(country))
        for unit in axis_and_allies_deck[index].get_units():
            generator = Generator(axis_and_allies_deck[index], unit)
            if full:
                generator.generate_back(output_folder=output_folder)
            generator.generate_front(output_folder=output_folder)
    except ValueError as e:
        logger.error(e)


def generate_from_file(file: str, output_folder: str = None, full: bool = False):
    """
    Generates units for countries listed in a new line delimited text file.
    :param file: files containing countries to generate for.
    :param output_folder: folder to dump the cards to, defaults to the current directory.
    :param full: whether to generate both the front and backs of the cards, defaults to false which generates only the
                 front.
    """
    countries_file = open(file, "r")
    for country in countries_file:
        generate_country(country.strip(), output_folder, full)
    countries_file.close()


def generate_single(country: str, unit: str, output_folder: str = None, full: bool = False):
    """
    Generates a single card for a single unit.
    :param country: name of country of the unit
    :param unit: name of the unit
    :param output_folder: output folder, defaults to the current directory.
    :param full: whether to generate both the front and backs of the cards, defaults to false which generates only the
                 front.
    """
    data_file = get_war_at_sea_json()
    data = json.load(data_file)
    axis_and_allies_deck = load_json(data)

    country_index = 0
    unit_index = 0
    for candidate_country in axis_and_allies_deck:
        if candidate_country.name == country:
            for candidate_unit in candidate_country.get_units():
                if candidate_unit.name == unit:
                    break
                else:
                    unit_index += 1
            break
        else:
            country_index += 1
    if country_index == len(axis_and_allies_deck) or \
            unit_index == len(axis_and_allies_deck[country_index].get_units()):
        logger.error("\"{}\" unit does not exist in for \"{}\"".format(unit, country))
        exit(1)

    generator = Generator(axis_and_allies_deck[country_index],
                          axis_and_allies_deck[country_index].get_units()[unit_index])
    if full:
        generator.generate_back(display=True, output_folder=output_folder)
    generator.generate_front(display=True, output_folder=output_folder)
    data_file.close()


if __name__ == '__main__':
    commands = {
        "generate_all": generate_all,
        "generate_country": generate_country,
        "generate_from_file": generate_from_file,
        "generate_single": generate_single
    }

    parser = argparse.ArgumentParser(prog="War at Sea Card Generator",
                                     description="Generate unit cards for the Axis and Allies War at Sea Naval "
                                                 "Miniatures game.",
                                     formatter_class=argparse.RawDescriptionHelpFormatter,
                                     )
    parser.add_argument("-l", "--log-level", required=False, default="INFO", help="Sets the logging level, defaults to"
                                                                                  " INFO.")
    subparsers = parser.add_subparsers(title="Available Commands", dest="command", metavar="command [options ...]")
    # ---------------------------------------  Generate All -------------------------------------
    generate_all_command = subparsers.add_parser("generate_all",
                                                 help="Generates the entire deck as defined by the "
                                                      "War at Sea data set.")
    generate_all_command.description = "Generate all units for all countries in the included War at Sea data set."
    generate_all_command.add_argument("-o", "--output-folder",
                                      help="Location to output the generated cards to, defaults to the current "
                                           "directory.")
    generate_all_command.add_argument("--full",
                                      help="Generates the front and back of the cards. By default only the front is"
                                           " generated.",
                                      default=False,
                                      action="store_true")
    # -------------------------------------  Generate Country ------------------------------------
    generate_country_command = subparsers.add_parser("generate_country",
                                                     help="Generates all units for a specified country")
    generate_country_command.description = "Generate all units for a specific country"
    generate_country_command.add_argument("-c", "--country", required=True,
                                          help="name of the country to generate units for")
    generate_country_command.add_argument("-o", "--output-folder",
                                          help="Location to output the generated cards to, defaults to the current "
                                               "directory.")
    generate_country_command.add_argument("--full",
                                          help="Generates the front and back of the cards. By default only the front is"
                                               " generated.",
                                          default=False,
                                          action="store_true")
    # ------------------------------------  Generate From File ------------------------------------
    generate_from_file_command = subparsers.add_parser("generate_from_file",
                                                       help="Generates all units for all countries"
                                                            " specified in a text file.")
    generate_from_file_command.description = "Generate all units for all countries specified in a new line delimited" \
                                             " text file."
    generate_from_file_command.add_argument("-f", "--file", required=True,
                                            help="countries file")
    generate_from_file_command.add_argument("-o", "--output-folder",
                                            help="Location to output the generated cards to, defaults to the current "
                                                 "directory.")
    generate_from_file_command.add_argument("--full",
                                            help="Generates the front and back of the cards. By default only the "
                                                 "front is generated.",
                                            default=False,
                                            action="store_true")
    # --------------------------------------  Generate Single -------------------------------------
    generate_single_command = subparsers.add_parser("generate_single",
                                                    help="Generate a single card for a single unit")
    generate_single_command.description = "Generate a single card for a single unit"
    generate_single_command.add_argument("-c", "--country", required=True,
                                         help="name of the country to generate units for")
    generate_single_command.add_argument("-u", "--unit", required=True,
                                         help="unit to generate")
    generate_single_command.add_argument("-o", "--output-folder",
                                         help="Location to output the generated cards to, defaults to the current "
                                              "directory.")
    generate_single_command.add_argument("--full",
                                         help="Generates the front and back of the cards. By default only the front is"
                                              " generated.",
                                         default=False,
                                         action="store_true")
    args = parser.parse_args()
    # check the log level
    logging.basicConfig(level=logging.getLevelName(args.log_level))

    # lookup the command
    command = commands[args.command]

    # store all arguments, then remove the command
    args = vars(args)
    del args["command"]
    del args["log_level"]

    # pass all remaining args as keyword args.
    command(**args)
