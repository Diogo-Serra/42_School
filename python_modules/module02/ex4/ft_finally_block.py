#!/usr/bin/env python3

class GardenError(Exception):
    pass


# Plant errors
class PlantError(GardenError):
    def __init__(self, message="The tomato plant is wilting!"):
        super().__init__(message)


def water_plant(plant_name):
    if plant_name == plant_name.capitalize():
        print(f"Watering plant: {plant_name}")
    else:
        raise PlantError(f"Error_Not_capitalized: {plant_name}")


def test_watering_system():
    print("=== Garden Watering System ===")

    print("\nTesting normal watering...")
    try:
        water_plant("tomato")
    except PlantError as e:
        print(f"{e}")
    finally:
        print("All tested")


if __name__ == '__main__':
    test_watering_system()
