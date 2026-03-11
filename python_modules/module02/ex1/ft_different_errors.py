#!/usr/bin/env python3

def garden_operations(operation: str) -> None:
    if operation == "value":
        int("abc")
    elif operation == "zero":
        1 / 0
    elif operation == "file":
        open("missing.txt")
    elif operation == "key":
        plant_data = {"rose": 25}
        print(plant_data["missing_plant"])


def test_error_types() -> None:
    print('=== Garden Error Types Demo ===\n')

    print("Testing ValueError...")
    try:
        garden_operations("value")
    except ValueError as e:
        print(f"Caught ValueError: {e}\n")
    print("Testing ZeroDivisionError...")
    try:
        garden_operations("zero")
    except ZeroDivisionError as e:
        print(f"Caught ZeroDivisionError: {e}\n")
    print("Testing FileNotFoundError...")
    try:
        garden_operations("file")
    except FileNotFoundError:
        print("Caught FileNotFoundError: No such file 'missing.txt'\n")
    print("Testing KeyError...")
    try:
        garden_operations("key")
    except KeyError as e:
        print(f"Caught KeyError: {e}\n")
    print("Testing multiple errors together...")
    try:
        garden_operations("value")
        garden_operations("zero")
    except (ValueError, ZeroDivisionError):
        print("Caught an error, but program continues!\n")
    print("All error types tested successfully!")


if __name__ == '__main__':
    test_error_types()
