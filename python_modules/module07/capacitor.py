#!/usr/bin/env python3
from ex1 import HealingCreatureFactory, TransformCreatureFactory


heal_factory = HealingCreatureFactory()
transform_factory = TransformCreatureFactory()
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
print(evolved.heal(base))

print("\nTesting Creature with transform capability")
transform_factory = TransformCreatureFactory()

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
