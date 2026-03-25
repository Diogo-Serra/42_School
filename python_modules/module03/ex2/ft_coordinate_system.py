#!/usr/bin/env python3

def get_player_pos() -> tuple[float, float, float]:
    while True:
        raw_coordinates: str = input(
            "Enter coordinates as floats in format 'x,y,z': "
        )

        parts: list[str] = [c.strip() for c in raw_coordinates.split(',')]
        if len(parts) != 3:
            print("Invalid syntax")
            continue

        coordinates_list: list[float] = []
        invalid_input: bool = False

        for part in parts:
            try:
                coordinates_list.append(float(part))
            except ValueError as e:
                print(f"Error on parameter '{part}': {e}")
                invalid_input = True
                break

        if invalid_input:
            continue

        return (coordinates_list[0], coordinates_list[1], coordinates_list[2])


def tester():
    print("=== Game Coordinate System ===")
    coordinates_center = (0, 0, 0)
    coordinates1: tuple[float, float, float] = get_player_pos()
    print(coordinates_center)
    print(coordinates1)


tester()
