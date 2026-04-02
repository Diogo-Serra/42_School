#!/usr/bin/env python3
import alchemy.transmutation as transmutation
from alchemy.transmutation import basic as b
from alchemy.transmutation import advanced as a

print("\n=== Pathway Debate Mastery ===\n")

print("Testing Absolute Imports (from basic.py):")
print(b.lead_to_gold())
print(b.stone_to_gem())

print("\nTesting Relative Imports (from advanced.py):")
print(a.philosophers_stone())
print(a.elixir_of_life())

print("\nTesting Package Access:")
print(f"alchemy.transmutation.lead_to_gold(): {transmutation.lead_to_gold()}")
print(f"alchemy.transmutation.philosophers_stone(): "
      f"{transmutation.philosophers_stone()}")

print("\nBoth pathways work! Absolute: clear, Relative: concise")
