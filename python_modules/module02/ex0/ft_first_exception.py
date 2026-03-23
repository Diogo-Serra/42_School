#!/usr/bin/env python3

def input_temperature(temp_str: str) -> int:
    try:
        temp_int: int = int(temp_str)
    except ValueError:
        raise ValueError(f"Error: '{temp_str}' is not a valid number\n")
    if temp_int < 0:
        raise ValueError(f"Error: {temp_int}°C is too cold for "
                         f"plants (min 0°C)\n")
    elif temp_int > 40:
        raise ValueError(f"Error: {temp_int}°C is too hot for "
                         f"plants (max 40°C)\n")
    else:
        return temp_int


def test_temperature() -> None:
    print('=== Garden Temperature Checker ===\n')
    test_data: list = [
        "25",
        "abc",
        "100",
        "-50"
    ]
    for test in test_data:
        print(f"Testing temperature: {test}")
        try:
            test_int: int = input_temperature(test)
            print(f"Temperature {test_int}°C is perfect for plants!\n")
        except ValueError as e:
            print(f"{e}\n")
    print('All tests completed - program didn\'t crash!')


if __name__ == '__main__':
    test_temperature()
