#!/usr/bin/env python3


class Plant:
    def __init__(self, name, water, sun):
        self.name = name
        self.water = water
        self.sun = sun


class GardenError(Exception):
    def __init__(self, message="Garden management error"):
        super().__init__(message)


class PlantError(GardenError):
    def __init__(self, message):
        super().__init__(message)


class WaterError(GardenError):
    def __init__(self, message="Not enough water in tank"):
        super().__init__(message)


class GardenManager:
    def __init__(self):
        self.garden_water = 2
        self.plant_list = []

    def add_plant(self, name: str, water: int, sun: int):
        if not name:
            raise PlantError("Error adding plant: Plant name cannot be empty!")
        plant = Plant(name, water, sun)
        self.plant_list.append(plant)
        print(f'Added {plant.name} successfully')

    def water_plant(self, plant):
        plant.water += 1
        self.garden_water -= 1
        print(f'Watering {plant.name} - success')

    def check_plant_health(self, plant) -> str:
        if plant.water < 1 or plant.water > 10:
            if plant.water < 1:
                raise PlantError(
                    f"Water level {plant.water} is too low (min 1)"
                )
            raise PlantError(f"Water level {plant.water} is too high (max 10)")
        if plant.sun < 2 or plant.sun > 12:
            if plant.sun < 2:
                raise PlantError(
                    f"Sunlight hours {plant.sun} is too low (min 2)"
                )
            raise PlantError(
                f"Sunlight hours {plant.sun} is too high (max 12)"
            )
        return (
            f"{plant.name}: healthy (water: {plant.water}, "
            f"sun: {plant.sun})"
        )

    def check_tank(self):
        if self.garden_water <= 0:
            raise WaterError()


def test_garden_management():
    print("=== Garden Management System ===\n")
    garden = GardenManager()
    plants_test = [
        ('tomato', 4, 8),
        ('lettuce', 14, 20),
        ('', 3, 8),
    ]
    print('Adding plants to garden...')
    for name, water, sun in plants_test:
        try:
            garden.add_plant(name, water, sun)
        except PlantError as e:
            print(e)
    print("\nWatering plants...")
    try:
        print('Opening watering system')
        for plant in garden.plant_list:
            garden.water_plant(plant)
    finally:
        print("Closing watering system (cleanup)\n")
    print("Checking plant health...")
    for plant in garden.plant_list:
        try:
            print(garden.check_plant_health(plant))
        except PlantError as e:
            print(f"Error checking {plant.name}: {e}")
    print("\nTesting error recovery...")
    try:
        garden.check_tank()
    except GardenError as e:
        print(f"Caught GardenError: {e}")
    finally:
        print("System recovered and continuing...")
    print("\nGarden management system test complete!")


if __name__ == '__main__':
    test_garden_management()
