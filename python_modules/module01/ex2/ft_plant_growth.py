#!/usr/bin/env python3

class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age


def grow(height: int) -> None:
    height += 1


def age(age: int) -> None:
    age += 1


def get_info(Plant) -> Plant:
    print(f"{plant.name}: {plant.height}cm, {plant.age} days old")

def ft_plant_growth() -> None:
    Plant("Rose", 25, 30)

 
if __name__ == "__main__":
    ft_plant_growth()
