#!/usr/bin/env python3

def ft_garden_summary() -> None:
    garden_name: str = str(input("Enter garden name: "))
    garden_plants: int = int(input("Enter number of plants: "))
    print(f"Garden: {garden_name}")
    print(f"Plants: {garden_plants}")
    print("Status: Growing well!")
