#!/usr/bin/env python3

def get_player_pos() -> tuple[float, float, float]:
    print("=== Game Coordinate System ===")
    while True:
        raw_coordinates: str = input(
            "Enter coordinates as floats in format 'x,y,z': "
        )

        try:
            coordinates: list[float] = [
                float(c.strip()) for c in raw_coordinates.split(',')]
            if len(coordinates) != 3:
                raise ValueError
            coordinates_tuple: tuple[float, float, float] = (
                tuple(coordinates)
            )
            break
        except ValueError:
            print("Error: please enter exactly 3 float values like x,y,z")
    return coordinates_tuple


def tester():
    coordinates: tuple[float, float, float] = get_player_pos()
    print(coordinates)


tester()
