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
        print("Testing artifact sorter...")
        sorted_artifacts = artifact_sorter(artifacts)
        print(
            f"{sorted_artifacts[0]['name']} ({sorted_artifacts[0]['power']} power)"
            f" comes before"
            f" {sorted_artifacts[1]['name']} ({sorted_artifacts[1]['power']} power)"
        )
        print("Testing spell transformer...")
        print(" ".join(spell_transformer(spells)))
    except Exception as e:
        print(e)
