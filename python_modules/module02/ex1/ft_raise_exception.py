#!/usr/bin/env python3

def input_temperature(temp_str: str) -> int:
    try:
        temp_int: int = int(temp_str)
    except ValueError:
        raise
    if temp_int < 0:
        raise ValueError(f"{temp_int}°C is too cold for "
                         f"plants (min 0°C)")
    elif temp_int > 40:
        raise ValueError(f"{temp_int}°C is too hot for "
                         f"plants (max 40°C)")
    else:
        print(f"Temperature is now {temp_int}°C")
        return temp_int


def test_temperature() -> None:
    print('=== Garden Temperature Checker ===')
    test_data: list = [
        "25",
        "abc",
        "100",
        -50
    ]
    for test in test_data:
        try:
            print(f"\nInput data is '{test}'")
            input_temperature(test)
        except ValueError as e:
            print(f"Caught input_temperature error: {e}")
    print('\nAll tests completed - program didn\'t crash!')


if __name__ == '__main__':
    test_temperature()
