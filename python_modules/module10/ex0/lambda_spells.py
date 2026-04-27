#!/usr/bin/env python3


artifacts = [
    {'name': "Fire staff", 'power': 98, 'type': "fire"},
    {'name': "Water staff", 'power': 76, 'type': "water"},
    {'name': "Dark staff", 'power': 100, 'type': "dark"}]

mages = [
    {'name': "Fire mage", 'power': 98, 'element': "fire"},
    {'name': "Water mage", 'power': 76, 'element': "water"},
    {'name': "Dark mage", 'power': 100, 'element': "dark"}]

spells = [
    "fireball",
    "heal",
    "shield"]


def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    return sorted(artifacts, key=lambda x: x['power'], reverse=True)


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    return filter(lambda x: x['power'] > min_power, mages)


def spell_transformer(spells: list[str]) -> list[str]:
    return map(lambda x: "* " + x + " *", spells)


def mage_stats(mages: list[dict]) -> dict:
    stats = {'max_power': int, 'min_power': int, 'avg_power': float}
    stats['max_power'] = max(mages, key=lambda x: x['power'])['power']
    stats['min_power'] = min(mages, key=lambda x: x['power'])['power']
    avg = sum(mage['power'] for mage in mages) / len(mages)
    stats['avg_power'] = round(avg, 2)
    return stats


try:
    for artifact in artifact_sorter(artifacts):
        print(artifact)
except Exception as e:
    print(e)

print()

try:
    for mage in power_filter(mages, 80):
        print(mage)
except Exception as e:
    print(e)

print()

try:
    for spell in spell_transformer(spell_transformer(spells)):
        print(spell)
except Exception as e:
    print(e)

print()

try:
    print(mage_stats(mages))
except Exception as e:
    print(e)
