#!/usr/bin/env python3

def input_temperature(temp_str: str) -> int:
    try:
        temp_int: int = int(temp_str)
    except ValueError:
        raise
    if temp_int < 0:
        raise ValueError(f"Error: {temp_int}°C is too cold for "
                         f"plants (min 0°C)\n")
    elif temp_int > 40:
        raise ValueError(f"Error: {temp_int}°C is too hot for "
                         f"plants (max 40°C)\n")
    else:
        print(f"Temperature is now {temp_int}°C")
        return temp_int


def test_temperature() -> None:
    print('=== Garden Temperature ===')
    test_data: list = [
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
