import json
import requests

from collections import OrderedDict
from specifications import NON_EXISTING_CARDS, \
    NON_EXISTING_PLAYTESTS, \
    LANGUAGE_IDS, \
    LANGUAGES, \
    ARTIST_PROOFS, \
    SPECIFIC_RARITIES, \
    GENERIC_RARITIES, \
    PLAYTESTS_SETS


def card_exists_in_set_language(set_name, language, foil):
    foil_param = "non-foil" if not foil else "foil"
    try:
        if (NON_EXISTING_CARDS[set_name][language][foil_param] and
                card_name in NON_EXISTING_CARDS[set_name][language][foil_param]) or \
                not NON_EXISTING_CARDS[set_name][language][foil_param]:
            return False
        return True
    except:
        return True


def is_common_or_uncommon_revised_card():
    for card_set in card_sets:
        if card_set["set_name"] == "Revised Edition" and "common" in card_set["rarity"]:
            return True
    return False


def is_common_or_uncommon_fourth_edition_card():
    for card_set in card_sets:
        if card_set["set_name"] == "Fourth Edition" and "common" in card_set["rarity"]:
            return True
    return False


print("Enter card name: ")
# card_name = input()
card_name = "Emrakul, the aeons torn"

request = f"https://api.scryfall.com/cards/named?fuzzy={'+'.join(card_name.split(' '))}"
r = requests.get(request)
card_data = json.loads(r.content)

try:
    card_id = card_data['oracle_id']
except KeyError:
    print("Specify a correct card name")
    exit(1)

request = f"https://api.scryfall.com/cards/search?order=released&q=oracleid%3A{card_id}&unique=prints"
r = requests.get(request)

card_sets = json.loads(r.content)['data']
card_prints = sorted([x for x in card_sets if x['games'] != ['mtgo']], key=lambda i: i['released_at'])
set_names = list(OrderedDict.fromkeys([card_set['set_name'] for card_set in card_prints]))

print(f"##### GlobalSet list for {card_name} #####")

counter = 1
print("Regular")
for set_name in set_names:
    for lang in LANGUAGES[set_name]:
        language = LANGUAGE_IDS[lang]
        if set_name == "Tenth Edition":
            a = 1
        if (['nonfoil'] in [x['finishes'] for x in card_sets if x['set_name'] == set_name]) or \
                (['nonfoil', 'foil'] in [x['finishes'] for x in card_sets if x['set_name'] == set_name]):
            if card_exists_in_set_language(set_name, language, foil=False):
                print(f"{counter} {set_name} [{language}]")
                counter += 1
        if ["foil"] in [x['finishes'] for x in card_sets if x['set_name'] == set_name] or \
                (['nonfoil', 'foil'] in [x['finishes'] for x in card_sets if x['set_name'] == set_name]) or \
                (['foil', 'nonfoil'] in [x['finishes'] for x in card_sets if x['set_name'] == set_name]):
            if card_exists_in_set_language(set_name, language, foil=True):
                print(f"{counter} {set_name} [{language}] (FOIL)")
                counter += 1

show_playtests_header = True
for set_name in set_names:
    if set_name in PLAYTESTS_SETS.keys() and card_name not in NON_EXISTING_PLAYTESTS.get(set_name, [card_name]):
        for playtest_name in PLAYTESTS_SETS[set_name]:
            if show_playtests_header:
                print("Playtests")
                show_playtests_header = False
            print(f"{counter} {playtest_name}")
            counter += 1

show_artist_proofs_header = True
for set_name in set_names:
    for ind, ap in enumerate(ARTIST_PROOFS.get(set_name, [])):
        if show_artist_proofs_header:
            print("Artist Proofs")
            show_artist_proofs_header = False
        print(f"{counter} {set_name} [{ap}]")
        counter += 1

print("Rarities")
for set_name in set_names:
    for rarity in SPECIFIC_RARITIES.get(set_name, []):
        print(f"{counter} {rarity}")
        counter += 1
    if set_name == "Revised Edition" and is_common_or_uncommon_revised_card():
        print(f"{counter} Revised Alpha Cut [English]")
        counter += 1
    if set_name == "Fourth Edition" and is_common_or_uncommon_fourth_edition_card():
        print(f"{counter} Fourth Edition Alpha Cut [English]")
        counter += 1
for rarity in GENERIC_RARITIES:
    print(f"{counter} {rarity}")
    counter += 1
