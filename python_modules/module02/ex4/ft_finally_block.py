#!/usr/bin/env python3

def water_plant(plant_name):
    try:
        if plant_name.upper():
            print(plant_name)
        else:
            print("1")


def test_watering_system():
    print("=== Garden Watering System ===")

    print("\nTesting normal watering...")
    water_plants(["tomato", "lettuce", "carrots"])
    print("Watering completed successfully!")

    print("\nTesting with error...")
    water_plants(["tomato", None, "lettuce"])
    print("\nCleanup always happens, even with errors!")


if __name__ == '__main__':
    test_watering_system()
