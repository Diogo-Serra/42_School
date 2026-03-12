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
    def __init__(self, message="Caught a garden error: "):
        super().__init__(message or type(self).__name__)


# Plant errors
class PlantError(GardenError):
    def __init__(self, message="Caught PlantError: The tomato plant is wilting!"):
        super().__init__(message)


# Water errors
class WaterError(GardenError):
    def __init__(self, message="Not enough water in the tank!"):
        super().__init__(message)


def custom_errors():
    print("=== Custom Garden Errors Demo ===")

    print("\nTesting PlantError...")
    try:
        Garden("Alice", "Ok", -1)
    except PlantError as e:
        print(f"{e}")

    print("\nTesting WaterError...")
    try:
        Garden("Bob", "dry", 5)
    except WaterError as e:
        print(f"Caught WaterError: {e}")

    print("\nTesting catching all garden errors...")
    for args in [("Alice", "Ok", -1), ("Bob", "dry", 5)]:
        try:
            Garden(*args)
        except GardenError as e:
            print(f"Caught a garden error: {e}")

    print("\nAll custom error types work correctly!")


def main():
    custom_errors()


if __name__ == '__main__':
    main()
