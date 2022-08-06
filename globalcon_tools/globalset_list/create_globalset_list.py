import json
import requests

from collections import OrderedDict
from globalcon_tools.globalset_list.specifications import NON_EXISTING_CARDS, \
    NON_EXISTING_PLAYTESTS, \
    LANGUAGE_IDS, \
    LANGUAGES, \
    ARTIST_PROOFS, \
    SPECIFIC_RARITIES, \
    GENERIC_RARITIES, \
    PLAYTESTS_SETS
from globalcon_tools import create_data_folders
from globalcon_tools.globalset_list.card import Card

global_set_card = Card()


def input_card_name():
    correct_card_name = False
    while not correct_card_name:
        print("Enter card name: ")
        card_name = input().title()

        request = f"https://api.scryfall.com/cards/named?fuzzy={'+'.join(card_name.split(' '))}"
        r = requests.get(request)
        card_data = json.loads(r.content)

        try:
            card_id = card_data['oracle_id']
            correct_card_name = True
        except KeyError:
            print("Specify a correct card name")
            exit(1)
    return global_set_card.set_card_data(card_name, card_id)


def card_exists_in_set_language(set_name, language, foil):
    foil_param = "non-foil" if not foil else "foil"
    try:
        if (NON_EXISTING_CARDS[set_name][language][foil_param] and
                global_set_card.card_name in NON_EXISTING_CARDS[set_name][language][foil_param]) or \
                not NON_EXISTING_CARDS[set_name][language][foil_param]:
            return False
        return True
    except:
        return True


def is_common_or_uncommon_revised_card():
    for card_set in global_set_card.card_sets:
        if card_set["set_name"] == "Revised Edition" and "common" in card_set["rarity"]:
            return True
    return False


def is_common_or_uncommon_fourth_edition_card():
    for card_set in global_set_card.card_sets:
        if card_set["set_name"] == "Fourth Edition" and "common" in card_set["rarity"]:
            return True
    return False


def generate_list():
    create_data_folders("globalset_list")

    input_card_name()

    request = \
        f"https://api.scryfall.com/cards/search?order=released&q=oracleid%3A{global_set_card.card_id}&unique=prints"
    r = requests.get(request)

    global_set_card.set_card_sets(json.loads(r.content)['data'])
    global_set_card.set_card_prints(
        sorted([x for x in global_set_card.card_sets if x['games'] != ['mtgo']], key=lambda i: i['released_at']))
    set_names = list(OrderedDict.fromkeys([card_set['set_name'] for card_set in global_set_card.card_prints]))

    globalset_list_file = open(f"DATA/GLOBALSET_LISTS/{global_set_card.card_name}.txt", "w")

    globalset_list_file.write(f"##### GlobalSet list for {global_set_card.card_name} #####\n")

    counter = 1
    globalset_list_file.write("Regular\n")
    for set_name in set_names:
        for lang in LANGUAGES[set_name]:
            language = LANGUAGE_IDS[lang]
            if (['nonfoil'] in [x['finishes'] for x in global_set_card.card_sets if x['set_name'] == set_name]) or \
               (['nonfoil', 'foil'] in [x['finishes'] for x in global_set_card.card_sets if x['set_name'] == set_name]):
                if card_exists_in_set_language(set_name, language, foil=False):
                    globalset_list_file.write(f"{counter} {set_name} [{language}]\n")
                    counter += 1
            if ["foil"] in [x['finishes'] for x in global_set_card.card_sets if x['set_name'] == set_name] or \
                    (['nonfoil', 'foil'] in [x['finishes'] for x in global_set_card.card_sets if x['set_name'] == set_name]) or \
                    (['foil', 'nonfoil'] in [x['finishes'] for x in global_set_card.card_sets if x['set_name'] == set_name]):
                if card_exists_in_set_language(set_name, language, foil=True):
                    globalset_list_file.write(f"{counter} {set_name} [{language}] (FOIL)\n")
                    counter += 1

    show_playtests_header = True
    for set_name in set_names:
        if set_name in PLAYTESTS_SETS.keys() and \
                global_set_card.card_name not in NON_EXISTING_PLAYTESTS.get(set_name, [global_set_card.card_name]):
            for playtest_name in PLAYTESTS_SETS[set_name]:
                if show_playtests_header:
                    globalset_list_file.write("Playtests\n")
                    show_playtests_header = False
                globalset_list_file.write(f"{counter} {playtest_name}\n")
                counter += 1

    show_artist_proofs_header = True
    for set_name in set_names:
        for ind, ap in enumerate(ARTIST_PROOFS.get(set_name, [])):
            if show_artist_proofs_header:
                globalset_list_file.write("Artist Proofs\n")
                show_artist_proofs_header = False
            globalset_list_file.write(f"{counter} {set_name} [{ap}]\n")
            counter += 1

    globalset_list_file.write("Rarities\n")
    for set_name in set_names:
        for rarity in SPECIFIC_RARITIES.get(set_name, []):
            globalset_list_file.write(f"{counter} {rarity}\n")
            counter += 1
        if set_name == "Revised Edition" and is_common_or_uncommon_revised_card():
            globalset_list_file.write(f"{counter} Revised Alpha Cut [English]\n")
            counter += 1
        if set_name == "Fourth Edition" and is_common_or_uncommon_fourth_edition_card():
            globalset_list_file.write(f"{counter} Fourth Edition Alpha Cut [English]\n")
            counter += 1
    for rarity in GENERIC_RARITIES:
        globalset_list_file.write(f"{counter} {rarity}\n")
        counter += 1
