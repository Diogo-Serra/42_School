#!/usr/bin/env python3

class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age


def ft_plant_types():
    my_plants = [Plant("Rose", 25, 30)]
    for plant in my_plants:
        print(f"{plant.name}: ({plant.height}cm, {plant.age} days)")


ft_plant_types()
