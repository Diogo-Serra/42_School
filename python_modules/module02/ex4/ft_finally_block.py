#!/usr/bin/env python3

# Garden errors
class GardenError(Exception):
    def __init__(self, message: str = "Unknown plant error") -> None:
        self.message = message


# Plant errors
class PlantError(GardenError):
    def __init__(self, message: str = "Unknown plant error") -> None:
        self.message = message


def water_plant(plant_name: str):
    if plant_name == plant_name.capitalize():
        print(f"Watering {plant_name}: [OK]")
    else:
        raise PlantError(
            f"Caught {PlantError.__name__}: Invalid plant name"
            f" to water: '{plant_name}'"
        )


def test_watering_system() -> None:
    valid_test: list[str] = [
        "Tomato",
        "Lettuce",
        "Carrots",
    ]

    invalid_test: list[str] = [
        "Tomato",
        "lettuce",
        "carrots",
    ]

    print("=== Garden Watering System ===")
    print("\nTesting valid plants...")
    print("Opening watering system")
    try:
        for test in valid_test:
            water_plant(test)
    except PlantError as e:
        print(f"{e}")
        print(".. ending tests and returning to main")
        return
    finally:
        print("Closing watering system")

    print("\nTesting invalid plants...")
    print("Opening watering system")
    try:
        for test in invalid_test:
            water_plant(test)
    except PlantError as e:
        print(f"{e}")
        print(".. ending tests and returning to main")
        return
    finally:
        print("Closing watering system")
        print("\nCleanup always happens, even with errors!")


if __name__ == '__main__':
    test_watering_system()
