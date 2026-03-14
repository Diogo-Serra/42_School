#!/usr/bin/env python3

class GardenManager:
    plant_list = []

    def add_plant(self, name, water, sun):
        print('Adding plants to garden...')
        if not name:
            raise ValueError("Error adding plant: Plant name cannot be empty!")
        plant = [name, water, sun]
        self.plant_list.append(plant)
        print(f'Added {self.name} successfully')
        print("")

    def water_plants(self):
        print("Watering plants...")
        print('Opening watering system')
        for plant in self.plant_list:
            print(f'Watering {plant.name} - success')
        print("Closing watering system (cleanup)")

    def check_plant_health(
        plant_name: str,
        water_level: int,
        sunlight_hours: int,
    ) -> str:
        if water_level < 1 or water_level > 10:
            if water_level < 1:
                raise ValueError(f"Water level {water_level} is too low"
                                 f"(min 1)")
            raise ValueError(f"Water level {water_level} is too high (max 10)")
        if sunlight_hours < 2 or sunlight_hours > 12:
            if sunlight_hours < 2:
                raise ValueError(f"Sunlight hours {sunlight_hours} is too low"
                                 f"(min 2)")
            raise ValueError(f"Sunlight hours {sunlight_hours} is too high"
                             f"(max 12)")
        return f"Plant '{plant_name}' is healthy!"

    def view_garden(self):
        for plant in self.plant_list:
            print(plant)


def test_garden_management():
    garden = GardenManager()
    garden.add_plant('tomato', 5, 8)
    garden.add_plant('lettuce', 15, 50)
    garden.add_plant('', 3, 8)
    garden.view_garden()
    garden.water_plants()
    garden.check_health()


test_garden_management()()
