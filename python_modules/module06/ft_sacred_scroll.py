#!/usr/bin/env python3
import alchemy

print("\n=== Sacred Scroll Mastery ===\n")

print("Testing direct module access:")

print(f"alchemy.elements.create_fire(): {alchemy.elements.create_fire()}")
print(f"alchemy.elements.create_water(): {alchemy.elements.create_water()}")
print(f"alchemy.elements.create_earth(): {alchemy.elements.create_earth()}")
print(f"alchemy.elements.create_air(): {alchemy.elements.create_air()}")

print("\nTesting package-level access (controlled by __init__.py):")

try:
    print(f"alchemy.elements.create_fire(): "
          f"{alchemy.elements.create_fire()}")
except AttributeError:
    print("alchemy.elements.create_fire(): AttributeError - not exposed")
try:
    print(f"alchemy.elements.create_water(): "
          f"{alchemy.elements.create_water()}")
except AttributeError:
    print("alchemy.elements.create_water(): AttributeError - not exposed")
try:
    print(f"alchemy.elements.create_earth(): "
          f"{alchemy.elements.create_earth()}")
except AttributeError:
    print("alchemy.elements.create_earth(): AttributeError - not exposed")
try:
    print(f"alchemy.elements.create_air(): "
          f"{alchemy.elements.create_air()}")
except AttributeError:
    print("alchemy.elements.create_air(): "
          "AttributeError - not exposed")

print("\nPackage metadata:")
print(f"Version: {alchemy.__version__}")
print(f"Author: {alchemy.__author__}")
