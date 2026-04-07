#!/usr/bin/env python3
from ex1 import HealingCreatureFactory


def test_factory():
    print("Testing Creature with healing capability")
    heal_factory = HealingCreatureFactory()
    sproutling = heal_factory.create_base()

    print(" base:")
    sproutling.describe()
    sproutling.attack()
    sproutling.heal()
