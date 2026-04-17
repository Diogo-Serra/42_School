#!/usr/bin/env python3


# def artifact_sorter(artifacts: list[dict]) -> list[dict]

print("Artifacts -----")

artifact = [
    {'name': "artifact3", "power": 3, 'art_type': "type1"},
    {'name': "artifact2", "power": 2, 'art_type': "type2"},
    {'name': "artifact6", "power": 6, 'art_type': "type3"},
    {'name': "artifact1", "power": 1, 'art_type': "type4"},
    {'name': "artifact4", "power": 4, 'art_type': "type5"},
]

artifact_sorter = list(
    sorted(artifact, key=lambda x: x['power'], reverse=True))
for dictx in artifact_sorter:
    print(dictx)

print("-----")
print("\nMages -----")


mages = [
    {'name': 'mage1', 'power': 1, 'element': 'fire'},
    {'name': 'mage2', 'power': 3, 'element': 'water'},
    {'name': 'mage3', 'power': 5, 'element': 'earth'},
    {'name': 'mage4', 'power': 2, 'element': 'air'},
    {'name': 'mage5', 'power': 4, 'element': 'dark'}]

min_power: list[int] = min([x['power'] for x in mages])
power_filter = list(
    filter(lambda x: x['power'] if x['power'] > min_power else
           False, artifact))
for mage in power_filter:
    print(mage)

print("-----")
print("\nSpells -----")

spells = [
    "fireball",
    "ember",
    "water gun",
    "hydro pump"]

spell_transformer = list(
    map(lambda x: '* ' + x + ' *', spells))
for spell in spell_transformer:
    print(spell)
