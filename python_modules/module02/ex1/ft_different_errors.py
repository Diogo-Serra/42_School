#!/usr/bin/env python3

def garden_operations() -> int:
    print("Testing ValueError...")
    try:
        int("abc")
    except ValueError:
        return 1
    try:
        1 / 0
    except ZeroDivisionError:
        return 2
    try:
        open("missing.txt")
    except FileNotFoundError:
        return 3
    try:
        plant_data = {"rose": 25}
        print(plant_data["missing_plant"])
    except KeyError as e:
        return 4
    try:
        int("abc")
        1 / 0
    except (ValueError, ZeroDivisionError):
        return 5


def test_error_types() -> None:
    print('=== Garden Error Types Demo ===\n')
    garden_operations()
    
    print(f"Caught ValueError: {e}\n")
    print("Testing ZeroDivisionError...")

    print(f"Caught ZeroDivisionError: {e}\n")
    print("Testing FileNotFoundError...")

    print("Caught FileNotFoundError: No such file 'missing.txt'\n")
    print("Testing KeyError...")


    print("Caught an error, but program continues!\n")
    print("All error types tested successfully!")
    print("All error types tested successfully!")


if __name__ == '__main__':
    test_error_types()
