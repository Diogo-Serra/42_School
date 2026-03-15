#!/usr/bin/env python3
from sys import argv
from math import sqrt

"""
=== Game Coordinate System ===

Position created: (10, 20, 5)
Distance between (0, 0, 0) and (10, 20, 5): 22.91

Parsing coordinates: "3,4,0"
Parsed position: (3, 4, 0)
Distance between (0, 0, 0) and (3, 4, 0): 5.0

Parsing invalid coordinates: "abc,def,ghi"
Error parsing coordinates: invalid literal for int() with base 10: 'abc'
Error details - Type: ValueError, Args: ("invalid literal for int()
with base 10: 'abc'",)

Unpacking demonstration:
Player at x=3, y=4, z=0
Coordinates: X=3, Y=4, Z=0
"""


def ft_coordinate_system():
    print("=== Game Coordinate System ===\n")
    if (len(argv) == 4):
        coordinates_list: list = []
        for data in argv[1:]:
            try:
                coordinate = int(data)
                coordinates_list.append(coordinate)
            except ValueError as e:
                print(f"Parsing invalid coordinates: "
                      f"\"{argv[1]},{argv[2]},{argv[3]}\"")
                print(f"Error parsing coordinates: {e}")
                print(f"Error details - {e}")
                return
        coords: tuple = tuple(coordinates_list)
        print(f"Position created: ({coords[0]}, {coords[1]}, {coords[2]})")
        diff: float = 0
        diff = sqrt((0-coords[1])**2 + (0-coords[2])**2 + (0-coords[3])**2)
        print(f"Distance between {coords} and (0, 0, 0): {diff}")
    else:
        print("Needs 3 coordinates")


ft_coordinate_system()
