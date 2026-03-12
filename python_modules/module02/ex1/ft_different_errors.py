#!/usr/bin/env python3

def garden_operations(input_str: type) -> None:
    if input_str == ValueError:
        int("abc")
    elif input_str == ZeroDivisionError:
        1 / 0
    elif input_str == FileNotFoundError:
        open("missing.txt")
    elif input_str == KeyError:
        plant_data = {"rose": 25}
        _ = plant_data["missing_plant"]
    elif input_str == "tests_value":
        int("abc")
    elif input_str == "tests_zero":
        1 / 0


def test_error_types() -> None:
    print('=== Garden Error Types Demo ===\n')
    error_messages = {
        ValueError: "Caught ValueError: invalid literal for int()",
        ZeroDivisionError: "Caught ZeroDivisionError: division by zero",
        FileNotFoundError: "Caught FileNotFoundError: "
        "No such file 'missing.txt'",
        KeyError: "Caught KeyError: 'missing_plant'",
    }
    for error_type, message in error_messages.items():
        try:
            print(f"Testing {error_type.__name__}...")
            garden_operations(error_type)
        except (ValueError, ZeroDivisionError, FileNotFoundError, KeyError):
            print(message + "\n")
    try:
        print("Testing multiple errors together...")
        garden_operations("tests_value")
        garden_operations("tests_zero")
    except (ValueError, ZeroDivisionError):
        print("Caught an error, but program continues!\n")
    print("All error types tested successfully!")


if __name__ == '__main__':
    test_error_types()
