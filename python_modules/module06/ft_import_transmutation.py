#!/usr/bin/env python3

# Full module
import alchemy.elements

# Specific function
from alchemy.elements import create_water

# Specific with alias
from alchemy.potions import healing_potion as heal

print("\n=== Import Transmutation Mastery ===\n")

print("Method 1 - Full module import:")
print(f"alchemy.elements.create_fire(): "
      f"{alchemy.elements.create_fire()}")


print("Method 2 - Specific function import:")
print(f"create_water(): {create_water()}")


print("Method 3 - Aliased import:")
print(f"heal(): {heal()}")
