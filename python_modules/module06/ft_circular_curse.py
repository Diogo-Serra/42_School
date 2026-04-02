#!/usr/bin/env python3
from alchemy.grimoire.validator import validate_ingredients
from alchemy.grimoire.spellbook import record_spell


print("\n=== Circular Curse Breaking ===\n")

print("Testing ingredient validation:")
print(f"validate_ingredients(\"fire air\"): "
      f"{validate_ingredients('fire air')}")
print(f"validate_ingredients(\"dragon scales\"): "
      f"{validate_ingredients('dragon scales')}")

print("\nTesting spell recording with validation:")
print(f"record_spell(\"Fireball\", \"fire air\"): "
      f"{record_spell('Fireball', 'fire air')}")
print(f"record_spell(\"Dark Magic\", \"shadow\"): "
      f"{record_spell('Dark Magic', 'shadow')}")

print("\nTesting late import technique:")
print(f"record_spell(\"Lightning\", \"air\"): "
      f"{record_spell('Lightning', 'air')}")

print("\nCircular dependency curse avoided using late imports!")
print("All spells processed safely!")
