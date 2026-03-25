#!/usr/bin/env python3
import math


def get_player_pos() -> tuple:
    print("=== Game Coordinate System ===")
    print("Get a first set of coordinates")
    while True:
        raw_coordinates: str = input(
            "Enter new coordinates as floats in format 'x,y,z': "
        )

        coordinates: list[str] = [c.strip() for c in raw_coordinates.split(',')]
        try:
            x: float = coordinates[0]
            y: float = coordinates[1]
            z: float = coordinates[2]
        except ValueError:
            raise ValueError('Erro')
        coordinates_tuple: tuple = tuple(coordinates)
        return coordinates_tuple


def tester():
    coordinates = get_player_pos()
    print(coordinates)
