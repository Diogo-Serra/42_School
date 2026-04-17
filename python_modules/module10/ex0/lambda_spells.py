#!/usr/bin/env python3

artifacts = [
    {'name': "Fire staff", 'power': 98, 'type': "fire"},
    {'name': "Water staff", 'power': 76, 'type': "water"},
    {'name': "Dark staff", 'power': 100, 'type': "dark"}]

mages = [
    {'name': "Fire mage", 'power': 98, 'element': "fire"},
    {'name': "Water mage", 'power': 76, 'element': "water"},
    {'name': "Dark mage", 'power': 100, 'element': "dark"}]


def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    return sorted(artifacts, key=lambda x: x['power'], reverse=True)


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    return filter(lambda x: x['power'] > min_power, mages)


def spell_transformer(spells: list[str]) -> list[str]:
    pass


def mage_stats(mages: list[dict]) -> dict:
    pass


for artifact in artifact_sorter(artifacts):
    print(artifact)

print()

for mage in power_filter(mages, 80):
    print(mage)
