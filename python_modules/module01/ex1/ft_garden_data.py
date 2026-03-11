#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: float, age: int):
        self.name = name
        self.height = height
        self.age = age

    def print_info(self):
        print(f"{self.name}: {self.height}cm, {self.age} days old")


def ft_garden_data():
    print("=== Garden Plant Registry ===")
    my_plants = [
        Plant("Rose", 25, 30),
        Plant("Sunflower", 80, 45),
        Plant("Cactus", 15, 120)]
    for plant in my_plants:
        plant.print_info()


if __name__ == "__main__":
    ft_garden_data()
