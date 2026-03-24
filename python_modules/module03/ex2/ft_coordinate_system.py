#!/usr/bin/env python3
import math


def prompt_coordinates() -> tuple[float, float, float]:
    while True:
        raw_coordinates = input(
            "Enter new coordinates as floats in format 'x,y,z': "
        )
        if raw_coordinates.count(',') != 2:
            print("Invalid syntax")
            continue

        first_comma = raw_coordinates.find(',')
        second_comma = raw_coordinates.find(',', first_comma + 1)

        x_raw = raw_coordinates[:first_comma].strip()
        y_raw = raw_coordinates[first_comma + 1:second_comma].strip()
        z_raw = raw_coordinates[second_comma + 1:].strip()

        try:
            x = float(x_raw)
            y = float(y_raw)
            z = float(z_raw)
            return (x, y, z)
        except ValueError as error:
            invalid_value = ""
            try:
                float(x_raw)
            except ValueError:
                invalid_value = x_raw
            else:
                try:
                    float(y_raw)
                except ValueError:
                    invalid_value = y_raw
                else:
                    invalid_value = z_raw
            print(f"Error on parameter '{invalid_value}': {error}")


def get_player_pos() -> None:
    print("=== Game Coordinate System ===")
    print("Get a first set of coordinates")
    first_coords = prompt_coordinates()
    print(f"Got a first tuple: {first_coords}")
    print(f"It includes: X={first_coords[0]}, Y={first_coords[1]}, "
          f"Z={first_coords[2]}")
    distance_to_center = math.sqrt(
        first_coords[0] ** 2 + first_coords[1] ** 2 + first_coords[2] ** 2
    )
    print(f"Distance to center: {distance_to_center:.4f}")
    print("Get a second set of coordinates")
    second_coords = prompt_coordinates()
    distance_between_points = math.sqrt(
        (second_coords[0] - first_coords[0]) ** 2
        + (second_coords[1] - first_coords[1]) ** 2
        + (second_coords[2] - first_coords[2]) ** 2
    )
    print("Distance between the 2 sets of coordinates: "
          f"{distance_between_points:.4f}")


get_player_pos()
