#!/usr/bin/env python3
from ex0.CreatureFactory import FlameFactory, AquaFactory


try:
    flame_f = FlameFactory()
    aqua_f = AquaFactory()
except Exception as e:
    print(f"Error creating factory: {e}")


def factory_tester(factory_object: FlameFactory | AquaFactory) -> None:

    print("Testing factory")

    try:
        base = factory_object.create_base()
        print(base.describe())
        print(base.attack())
    except Exception as e:
        print(f"Error with base instance: {e}")

    try:
        evolved = factory_object.create_evolved()
        print(evolved.describe())
        print(evolved.attack())
    except Exception as e:
        print(f"Error with evolved instance: {e}")


def combat_tester(flame_f: FlameFactory, aqua_f: AquaFactory) -> None:

    print("Testing battle")

    flameling = flame_f.create_base()
    aquabub = aqua_f.create_base()
    print(flameling.describe())
    print(" vs.")
    print(aquabub.describe())
    print(" fight!")
    try:
        print(flameling.attack())
        print(aquabub.attack())
    except Exception as e:
        print(f"Error on attack phase{e}")


factory_tester(flame_f)
print()
factory_tester(aqua_f)
print()
combat_tester(flame_f, aqua_f)
