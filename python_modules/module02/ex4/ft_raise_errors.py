#!/usr/bin/env python3


def check_plant_health(
    plant_name: str,
    water_level: int,
    sunlight_hours: int,
) -> str:
    if not plant_name:
        raise ValueError("Plant name cannot be empty.")
    if water_level < 1 or water_level > 10:
        if water_level < 1:
            raise ValueError(f"Water level {water_level} is too low (min 1)")
        raise ValueError(f"Water level {water_level} is too high (max 10)")
    if sunlight_hours < 2 or sunlight_hours > 12:
        if sunlight_hours < 2:
            raise ValueError(f"Sunlight hours {sunlight_hours} is too low"
                             f"(min 2)")
        raise ValueError(f"Sunlight hours {sunlight_hours} is too high"
                         f"(max 12)")
    return f"Plant '{plant_name}' is healthy!"


def test_plant_checks():
    """Demonstrate valid and invalid cases using try/except/finally."""
    print("=== Garden Plant Health Checker ===")
    tests = [
        ("\nTesting good values...", "tomato", 5, 6),
        ("\nTesting empty plant name...", "", 5, 6),
        ("\nTesting bad water level...", "tomato", 15, 6),
        ("\nTesting bad sunlight hours...", "tomato", 5, 0),
    ]

    for label, name, water, sunlight in tests:
        print(label)
        try:
            print(check_plant_health(name, water, sunlight))
        except ValueError as e:
            print(f"Error: {e}")
    print("\nAll error raising tests completed!")


if __name__ == '__main__':
    test_plant_checks()
