#!/usr/bin/env python3

def ft_plant_age() -> None:
    age: int = int(input("Enter plant's age: "))
    if age <= 60:
        print("Plant needs more time to grow.")
    else:
        print("Plant is ready to harvest.")


ft_plant_age()
