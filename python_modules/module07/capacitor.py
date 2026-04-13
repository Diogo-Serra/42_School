#!/usr/bin/env python3
from ex1 import HealingCreatureFactory, TransformCreatureFactory


def test_heal_factory() -> None:

    heal_factory = HealingCreatureFactory()

    print("Testing Creature with healing capability")

    print(" base:")
    base = heal_factory.create_base()
    print(base.describe())
    print(base.attack())
    print(base.heal(base))

    print(" evolved:")
    evolved = heal_factory.create_evolved()
    print(evolved.describe())
    print(evolved.attack())
    print(evolved.heal())


def test_transform_factory() -> None:

    transform_factory = TransformCreatureFactory()

    print("Testing Creature with transform capability")

    print(" base:")
    shiftling = transform_factory.create_base()
    print(shiftling.describe())
    print(shiftling.attack())
    print(shiftling.transform())
    print(shiftling.attack())
    print(shiftling.revert())

    print(" evolved:")
    morphagon = transform_factory.create_evolved()
    print(morphagon.describe())
    print(morphagon.attack())
    print(morphagon.transform())
    print(morphagon.attack())
    print(morphagon.revert())


test_heal_factory()
print()
test_transform_factory()
