#!/usr/bin/env python3

# Garden errors
class GardenError(Exception):
    def __init__(self, message: str = "Unknown plant error") -> None:
        self.message = message


# Plant errors
class PlantError(GardenError):
    message: str = "Unknown plant error"


# Water errors
class WaterError(GardenError):
    message: str = "Unknown plant error"


class Garden:
    def __init__(self, owner: str, status: str, plants: int):
        if plants < 0:
            raise PlantError("The tomato plant is wilting!")
        if status == "dry":
            raise WaterError("Not enough water in the tank")
        self.owner = owner
        self.status = status
        self.plants = plants


def custom_errors() -> None:
    print("=== Custom Garden Errors Demo ===")

    print("\nTesting PlantError...")
    try:
        Garden("Alice", "Ok", -1)
    except PlantError as e:
        print(f"Caught {type(e).__name__}: {e.message}")

    print("\nTesting WaterError...")
    try:
        Garden("Bob", "dry", 5)
    except WaterError as e:
        print(f"Caught {type(e).__name__}: {e.message}")

    print("\nTesting catching all garden errors...")
    try:
        Garden("Alice", "Ok", -1)
    except GardenError as e:
        print(f"Caught GardenError: {e.message}")
    try:
        Garden("Bob", "dry", 5)
    except GardenError as e:
        print(f"Caught GardenError: {e.message}")
    print("\nTesting catching all garden errors...")


def main():
    custom_errors()


if __name__ == '__main__':
    main()
