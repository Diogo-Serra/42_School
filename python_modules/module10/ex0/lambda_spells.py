#!/usr/bin/env python3


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
    from data_generator import FuncMageDataGenerator
    artifacts = FuncMageDataGenerator.generate_artifacts(5)
    mages = FuncMageDataGenerator.generate_mages(5)
    spells = FuncMageDataGenerator.generate_spells(5)

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
