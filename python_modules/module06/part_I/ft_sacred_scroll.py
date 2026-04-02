#!/usr/bin/env python3
import alchemy

print("=== Sacred Scroll Mastery ===\n")

print("Testing direct module access:")

print(f"alchemy.elements.create_fire(): {alchemy.elements.create_fire()}")
print(f"alchemy.elements.create_water(): {alchemy.elements.create_water()}")
print(f"alchemy.elements.create_earth(): {alchemy.elements.create_earth()}")
print(f"alchemy.elements.create_air(): {alchemy.elements.create_air()}")

print("Testing package-level access (controlled by __init__.py):\n")

try:
    print(f"alchemy.elements.create_fire(): {alchemy.create_fire()}")
except AttributeError:
    print("alchemy.elements.create_fire(): AttributeError - not exposed")
try:
    print(f"alchemy.elements.create_water(): {alchemy.create_water()}")
except AttributeError:
    print("alchemy.elements.create_water(): AttributeError - not exposed")
try:    
    print(f"alchemy.elements.create_earth(): {alchemy.create_earth()}")
except AttributeError:
    print("alchemy.elements.create_earth(): AttributeError - not exposed")
try:
    print(f"alchemy.elements.create_air(): {alchemy.create_air()}")
except AttributeError:
    print("alchemy.elements.create_air(): AttributeError - not exposed")
