#!/usr/bin/env python3
'''
• Checks if the plant name is valid (not empty)
• Checks if water level is reasonable (between 1 and 10)
• Checks if sunlight hours are reasonable (between 2 and 12)
• Raises appropriate errors with helpful messages when something is wrong
• Returns a success message if everything is okay
'''


def check_plant_health(plant_name, water_level, sunlight_hours):
    if not plant_name:
        print("Plant name is empty.")
 

def test_plant_checks():
    check_plant_health("te", 12, 4)


if __name__ == '__main__':
    test_plant_checks()
