#!/usr/bin/env python3
from ex1.Healing_Creatures import HealingCreatureFactory


def test_factory():
    print("Testing Creature with healing capability")
    heal_factory = HealingCreatureFactory()
    sproutling = heal_factory.create_base()

    print(" base:")
    print(sproutling.describe())
    print(sproutling.attack())
    print(sproutling.heal())
    print(" evolved:")

    bloomelle = heal_factory.create_evolved()
    print(bloomelle.describe())
    print(bloomelle.attack())
    print(bloomelle.heal())


test_factory()
