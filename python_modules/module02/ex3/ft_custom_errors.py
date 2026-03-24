#!/usr/bin/env python3

# Simple class for testing
class Garden:
    def __init__(self, owner: str, status: str, plants: int):
        if plants < 0:
            raise PlantError()
        if status == "dry":
            raise WaterError()
        self.owner = owner
        self.status = status
        self.plants = plants


# Garden errors
class GardenError(Exception):
    message = "Unknown plant error"


# Plant errors
class PlantError(GardenError):
    message = "The tomato plant is wilting!"


# Water errors
class WaterError(GardenError):
    message = "Not enough water in the tank"


def custom_errors() -> None:
    print("=== Custom Garden Errors Demo ===")

    garden_data: list[tuple] = [
        ("Alice", "Ok", -1),
        ("Bob", "dry", 5),
    ]

    print("\nTesting PlantError...")
    try:
        Garden(*garden_data[0])
    except PlantError as e:
        print(f"Caught {type(e).__name__}: {e.message}")

    print("\nTesting WaterError...")
    try:
        Garden(*garden_data[1])
    except WaterError as e:
        print(f"Caught {type(e).__name__}: {e.message}")

    print("\nTesting catching all garden errors...")
    for garden in garden_data:
        try:
            Garden(*garden)
        except GardenError as e:
            print(f"Caught GardenError: {e.message}")

    print("\nTesting catching all garden errors...")


def main():
    custom_errors()


if __name__ == '__main__':
    main()
