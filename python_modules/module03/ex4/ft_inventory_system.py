#!/usr/bin/env python3
import sys


def parse_inventory(arguments: list[str]) -> dict[str, int]:
    inventory: dict[str, int] = {}

    for parameter in arguments:
        if parameter.count(":") != 1:
            print(f"Error - invalid parameter '{parameter}'")
            continue
        item_name, quantity_text = parameter.split(":")
        if not item_name or not quantity_text:
            print(f"Error - invalid parameter '{parameter}'")
            continue
        if item_name in inventory:
            print(f"Redundant item '{item_name}' - discarding")
            continue
        try:
            quantity = int(quantity_text)
        except ValueError as error:
            print(f"Quantity error for '{item_name}': {error}")
            continue
        inventory[item_name] = quantity
    return inventory


def get_most_abundant(inventory: dict[str, int]) -> tuple[str, int]:
    first_item = list(inventory.keys())[0]
    most_name = first_item
    most_quantity = inventory[first_item]

    for item_name in inventory:
        if inventory[item_name] > most_quantity:
            most_name = item_name
            most_quantity = inventory[item_name]
    return most_name, most_quantity


def get_least_abundant(inventory: dict[str, int]) -> tuple[str, int]:
    first_item = list(inventory.keys())[0]
    least_name = first_item
    least_quantity = inventory[first_item]

    for item_name in inventory:
        if inventory[item_name] < least_quantity:
            least_name = item_name
            least_quantity = inventory[item_name]
    return least_name, least_quantity


def ft_inventory_system(inventory: dict[str, int]) -> None:
    item_list = list(inventory.keys())
    total_quantity = sum(inventory.values())

    print(f"Got inventory: {inventory}")
    print(f"Item list: {item_list}")
    print(f"Total quantity of the {len(item_list)} items: {total_quantity}")

    for item_name in inventory:
        percentage = round(inventory[item_name] * 100 / total_quantity, 1)
        print(f"Item {item_name} represents {percentage}%")

    if inventory:
        most_name, most_quantity = get_most_abundant(inventory)
        least_name, least_quantity = get_least_abundant(inventory)
        print(f"Item most abundant: {most_name} with quantity {most_quantity}")
        print(
            f"Item least abundant: {least_name} with quantity {least_quantity}"
        )

    inventory.update({"magic_item": 1})
    print(f"Updated inventory: {inventory}")


def main() -> None:
    print("=== Inventory System Analysis ===")
    inventory = parse_inventory(sys.argv[1:])
    ft_inventory_system(inventory)


main()
