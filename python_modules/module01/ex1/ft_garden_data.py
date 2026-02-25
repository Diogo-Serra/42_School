#!/usr/bin/env python3

class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age


def print_Plant(plants):
    for plant in plants:
        print(f"{plant.name}: {plant.height}cm, {plant.age} days old")


def ft_garden_data():
    print("=== Garden Plant Registry ===")
    my_Plants = [
        Plant("Rose", 25, 30),
        Plant("Sunflower", 80, 45),
        Plant("Cactus", 15, 120)]
    print_Plant(my_Plants)


if __name__ == "__main__":
    ft_garden_data()
