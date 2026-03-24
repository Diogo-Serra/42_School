#!/usr/bin/env python3

def input_temperature(temp_str: str) -> int:
    temp_int: int = int(temp_str)
    print(f"Temperature is now {temp_int}°C")
    return temp_int


def test_temperature() -> None:
    print('=== Garden Temperature ===')
    test_data: list[str] = [
        "25",
        "abc",
    ]
    for test in test_data:
        try:
            print(f"\nInput data is '{test}'")
            input_temperature(test)
        except ValueError as e:
            print(f"Caught input_temperature error: {e}\n")
    print('All tests completed - program didn\'t crash!')


if __name__ == '__main__':
    test_temperature()
