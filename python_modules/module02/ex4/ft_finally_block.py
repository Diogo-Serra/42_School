#!/usr/bin/env python3

def water_plant(plant_name):
    try:
        if plant_name.upper():
            print(plant_name)
        else:
            print("1")
    except ValueError as e:
        raise e


def test_watering_system():
    print("=== Garden Watering System ===")

    print("\nTesting normal watering...")
    water_plant("tomato")


if __name__ == '__main__':
    test_watering_system()
