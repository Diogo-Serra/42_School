#!/usr/bin/env python3
from sys import exit


def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    return list(sorted(artifacts, key=lambda x: x['power'], reverse=True))


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    return list(filter(lambda x: x['power'] >= min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:
    return list(map(lambda x: "* " + x + " *", spells))


def mage_stats(mages: list[dict]) -> dict:
    stats = {'max_power': int, 'min_power': int, 'avg_power': float}
    stats['max_power'] = max(mages, key=lambda x: x['power'])['power']
    stats['min_power'] = min(mages, key=lambda x: x['power'])['power']
    avg = sum(mage['power'] for mage in mages) / len(mages)
    stats['avg_power'] = round(avg, 2)
    return stats


if __name__ == "__main__":

    try:

        artifacts = [
            {'name': 'Storm Crown', 'power': 74, 'type': 'armor'},
            {'name': 'Fire Staff', 'power': 102, 'type': 'armor'},
            {'name': 'Lightning Rod', 'power': 115, 'type': 'focus'},
            {'name': 'Light Prism', 'power': 67, 'type': 'relic'}]

        mages = [
            {'name': 'Riley', 'power': 61, 'element': 'lightning'},
            {'name': 'Ember', 'power': 87, 'element': 'ice'},
            {'name': 'Morgan', 'power': 61, 'element': 'water'},
            {'name': 'River', 'power': 76, 'element': 'lightning'},
            {'name': 'Zara', 'power': 89, 'element': 'lightning'}]

        spells = ['tsunami', 'flash', 'lightning', 'blizzard']

    except Exception as error:
        print(error)
        exit(1)

    try:
        print()

        print("Testing artifact sorter...")
        sorted_artifacts = artifact_sorter(artifacts)
        print(
            f"{sorted_artifacts[0]['name']} "
            f"({sorted_artifacts[0]['power']} power)"
            f" comes before"
            f" {sorted_artifacts[1]['name']} "
            f"({sorted_artifacts[1]['power']} power)")

        print()

        print("Testing mage filter...")
        mages_filter = power_filter(mages, 80)
        if not mages_filter:
            print("No mages with this power")
        for mage in mages_filter:
            print(mage)

        print()

        print("Testing spell transformer...")
        print(" ".join(spell_transformer(spells)))

        print()

        print("Testing mage stats...")
        stats_mage = mage_stats(mages)
        print(stats_mage)

    except Exception as error:
        print(error)
        exit(1)
