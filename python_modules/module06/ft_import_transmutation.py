#!/usr/bin/env python3

# Full module
import alchemy.elements

# Specific function
from alchemy.elements import create_water
from alchemy.potions import strength_potion

# Specific with alias
from alchemy.potions import healing_potion as heal

# Multiple imports
from alchemy.elements import create_earth, create_fire

print("\n=== Import Transmutation Mastery ===\n")

print("Method 1 - Full module import:")
print(f"alchemy.elements.create_fire(): "
      f"{alchemy.elements.create_fire()}")


print("Method 2 - Specific function import:")
print(f"create_water(): {create_water()}")


print("Method 3 - Aliased import:")
print(f"heal(): {heal()}")


print("Method 4 - Multiple imports:")
print(f"create_earth(): {create_earth()}")
print(f"fire(): {create_fire()}")
print(f"strength_potion(): {strength_potion()}")

print("All import transmutation methods mastered!")
