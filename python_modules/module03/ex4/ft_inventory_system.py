#!/usr/bin/env python3

"""
=== Inventory System Analysis ===
Total items in inventory: 12
Unique item types: 5
=== Current Inventory ===
potion: 5 units (41.7%)
armor: 3 units (25.0%)
shield: 2 units (16.7%)
sword: 1 unit (8.3%)
helmet: 1 unit (8.3%)
=== Inventory Statistics ===
Most abundant: potion (5 units)
Least abundant: sword (1 unit)
=== Item Categories ===
Moderate: {'potion': 5}
Scarce: {'sword': 1, 'shield': 2, 'armor': 3, 'helmet': 1}
=== Management Suggestions ===
Restock needed: sword, helmet
=== Dictionary Properties Demo ===
Dictionary keys: sword, potion, shield, armor, helmet
Dictionary values: 1, 5, 2, 3, 1
Sample lookup - 'sword' in inventory: True
"""


def ft_inventory_system(inventory):
    print("\n=== Current Inventory ===")
    inventory_keys = inventory.keys()
    inventory_values = inventory.values()
    for k, v in zip(inventory_keys, inventory_values):
        print(f"{k}: {v} ({round(v * 100 / sum(inventory_values), 1)})")


def main():
    inventory = {
        "potion": 5,
        "armor": 3,
        "shield": 2,
        "sword": 1,
        "helmet": 1,
    }
    print("=== Dictionary Properties Demo ===")
    inventory_keys = inventory.keys()
    inventory_values = inventory.values()
    print(f"Total inventory in inventory: {sum(inventory_values)}")
    print(f"Unique item types: {len(inventory_keys)}")
    ft_inventory_system(inventory)


main()
