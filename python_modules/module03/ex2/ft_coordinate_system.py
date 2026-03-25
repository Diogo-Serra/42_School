#!/usr/bin/env python3
from math import sqrt


def get_player_pos() -> tuple[float, float, float]:
    while True:
        raw_coordinates: str = input(
            "Enter new coordinates as floats in format 'x,y,z': "
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

        tuple(coordinates_list)
        return (coordinates_list)


def tester():
    print("=== Game Coordinate System ===")
    ccenter = (0, 0, 0)
    ccx: float = ccenter[0]
    ccy: float = ccenter[1]
    ccz: float = ccenter[2]

    print("\nGet a first set of coordinates")
    c1: tuple[float, float, float] = get_player_pos()
    print(f"Got a first tuple: {c1}")

    x1: float = c1[0]
    y1: float = c1[1]
    z1: float = c1[2]
    print(f"It includes: X={x1}, Y={y1}, Z={z1}")
    distance_center = sqrt((x1 - ccx)**2 + (y1 - ccy)**2 + (z1 - ccz))
    print(f"Distance to center: {round(distance_center, 4)}")

    print("\nGet a second set of coordinates")
    c2: tuple[float, float, float] = get_player_pos()
    x2: float = c2[0]
    y2: float = c2[1]
    z2: float = c2[2]
    distance_two = sqrt((x1 - x2)**2 + (y1 - y2)**2 + (z1 - z2))
    print(f"Distance between the 2 sets of coordinates: {distance_two}")


tester()
