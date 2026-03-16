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
    total_value = sum(inventory.values())
    inventory_values = inventory.values()
    print("\n=== Current Inventory ===")
    for item in inventory:
        if inventory.get(item) > 1:
            print(f"{item}: {inventory.get(item)} units "
                  f"({round(inventory.get(item) * 100 / total_value, 1)}%)")
        else:
            print(f"{item}: {inventory.get(item)} unit "
                  f"({round(inventory.get(item) * 100 / total_value, 1)}%)")
    print("\n=== Inventory Statistics ===")
    print(f"Most abundant: potion ({max(inventory_values)} units)")
    print(f"Least abundant: sword ({min(inventory_values)} unit)")
    print("=== Item Categories ===")
    moderate = {}
    scarce = {}
    for item, count in inventory.items():
        if count >= 5:
            moderate[item] = count
        elif count <= 3:
            scarce[item] = count

    print(f"Moderate: {moderate}")
    print(f"Scarce: {scarce}")
    print("=== Management Suggestions ===")
    restock_needed = [item for item, count in inventory.items() if count <= 1]
    print(f"Restock needed: {', '.join(restock_needed)}")

    print("=== Dictionary Properties Demo ===")
    print(f"Dictionary keys: {', '.join(inventory.keys())}")
    values_str = ', '.join(str(value) for value in inventory.values())
    print(f"Dictionary values: {values_str}")
    print(f"Sample lookup - 'sword' in inventory: {'sword' in inventory}")


def main():
    inventory = {
        "potion": 5,
        "armor": 3,
        "shield": 2,
        "sword": 1,
        "helmet": 1,
    }
    print("=== Inventory System Analysis ===")
    inventory_keys = inventory.keys()
    inventory_values = inventory.values()
    print(f"Total items in inventory: {sum(inventory_values)}")
    print(f"Unique item types: {len(inventory_keys)}")
    ft_inventory_system(inventory)


main()
