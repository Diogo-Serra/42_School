#!/usr/bin/env python3

def check_temperature(temp_str: str) -> int:
    try:
        temp_int: int = int(temp_str)
    except ValueError:
        return f"Error: '{temp_str}' is not a valid number\n"
    if temp_int < 0:
        return f"Error: {temp_int}°C is too cold for plants (min 0°C)\n"
    elif temp_int > 40:
        return f"Error: {temp_int}°C is too hot for plants (max 40°C)\n"
    else:
        return temp_int


def test_temperature_input():
    print('=== Garden Temperature Checker ===\n')
    test_data: list = [
        "25",
        "abc",
        "100",
        "-50"
    ]
    for i in test_data:
        test: int = check_temperature(i)
        print(f"Testing temperature: {i}")
        if isinstance(test, int):
            print(f"Temperature {test}°C is perfect for plants!\n")
        else:
            print(test)
    print('All tests completed - program didn\'t crash!')


if __name__ == '__main__':
    test_temperature_input()
