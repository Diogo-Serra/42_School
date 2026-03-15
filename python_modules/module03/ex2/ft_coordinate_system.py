#!/usr/bin/env python3
from sys import argv
from math import sqrt


def ft_coordinate_system():
    print("=== Game Coordinate System ===\n")
    if (len(argv) == 4):
        coordinates_list: list = []
        print(f"Parsing coordinates: \"{argv[1]},{argv[2]},{argv[3]}\"")
        for data in argv[1:]:
            try:
                coordinate = int(data)
                coordinates_list.append(coordinate)
            except ValueError as e:
                print(f"Parsing invalid coordinates: "
                      f"\"{argv[0]},{argv[1]},{argv[2]}\"")
                print(f"Error parsing coordinates: {e}")
                print(f"Error details - {e}")
                return
        coords: tuple = tuple(coordinates_list)
        print(f"Parsed position: ({coords[0]}, {coords[1]}, {coords[2]})")
        print(f"Position created: ({coords[0]}, {coords[1]}, {coords[2]})")
        diff: float = 0
        diff = sqrt((0-coords[0])**2 + (0-coords[1])**2 + (0-coords[2])**2)
        print(f"Distance between {coords} and (0, 0, 0): {diff}")
        print("\nUnpacking demonstration:")
        x, y, z = coords
        print(f"Player at: x={x}, y={y}, z={z}")
        print(f"Coordinates: X={x}, Y={y}, Z={z}")
    else:
        print("Needs 3 coordinates")


ft_coordinate_system()
