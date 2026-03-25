#!/usr/bin/env python3

def get_player_pos() -> list[tuple[float, float, float]]:
    print("=== Game Coordinate System ===")
    coordinates_float: list[tuple[float, float, float]] = []
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
            coordinates_float.append(coordinates_tuple)
            break
        except ValueError:
            print("Error: please enter exactly 3 float values like x,y,z")
    return coordinates_float


def tester():
    coordinates: list[tuple[float, float, float]] = get_player_pos()
    print(coordinates)


tester()
