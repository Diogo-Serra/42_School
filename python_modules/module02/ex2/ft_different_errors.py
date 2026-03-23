#!/usr/bin/env python3

def garden_operations(operation_number: int) -> None:
    try:
        if operation_number == 0:
            int("abc")
        elif operation_number == 1:
            10 / 0
        elif operation_number == 2:
            with open("/non/existent/file", "r", encoding="utf-8"):
                pass
        elif operation_number == 3:
            plant: str = "tomato"
            print(plant + 1)
        else:
            return
    except (ValueError, ZeroDivisionError, FileNotFoundError, TypeError):
        raise


def test_error_types() -> None:
    print("=== Garden Error Types Demo ===")
    test_list: list[tuple] = [
        ("ValueError", 0),
        ("ZeroDivisionError", 1),
        ("FileNotFoundError", 2),
        ("TypeError", 3),
        ("", 4)
    ]
    for test in test_list:
        print(f"Testing operation {test[1]}...")
        try:
            garden_operations(test[1])
        except (ValueError, ZeroDivisionError, FileNotFoundError, TypeError) as e:
            print(f"Caught {type(e).__name__}: {e}")
    print("Operation completed successfully")
    print("\nAll error types tested successfully!")


if __name__ == '__main__':
    test_error_types()
