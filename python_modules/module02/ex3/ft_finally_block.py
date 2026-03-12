#!/usr/bin/env python3

def water_plants(plant_list):
    try:
        print("Opening watering system")
        for plant in plant_list:
            if not isinstance(plant, str) or not plant.isalpha():
                raise ValueError(f"Cannot water {plant} - invalid plant!")
            print(f"Watering {plant}")
    except ValueError as e:
        print(f"Error: {e}")
    finally:
        print("Closing watering system (cleanup)")


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
