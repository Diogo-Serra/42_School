#!/usr/bin/env python3

def garden_operations(error_type: str) -> None:
    if error_type == "value":
        int("abc")
    elif error_type == "zero":
        10 / 0
    elif error_type == "file":
        with open("missing.txt", "r", encoding="utf-8"):
            pass
    elif error_type == "key":
        plants = {"tomato": 12, "carrot": 8}
        print(plants["missing_plant"])


def test_error_types() -> None:
    print("=== Garden Error Types Demo ===\n")

    print("Testing ValueError...")
    try:
        garden_operations("value")
    except ValueError:
        print("Caught ValueError: invalid literal for int()\n")

    print("Testing ZeroDivisionError...")
    try:
        garden_operations("zero")
    except ZeroDivisionError as error:
        print(f"Caught ZeroDivisionError: {error}\n")

    print("Testing FileNotFoundError...")
    try:
        garden_operations("file")
    except FileNotFoundError:
        print("Caught FileNotFoundError: No such file 'missing.txt'\n")

    print("Testing KeyError...")
    try:
        garden_operations("key")
    except KeyError as error:
        print(f"Caught KeyError: {error}\n")

    try:
        print("Testing multiple errors together...")
        garden_operations("value")
        garden_operations("zero")
    except (ValueError, ZeroDivisionError):
        print("Caught an error, but program continues!\n")

    print("All error types tested successfully!")


if __name__ == '__main__':
    test_error_types()
