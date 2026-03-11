#!/usr/bin/env python3

# A class bundles data and behavior together
# objects are the instances of that class blueprint.
class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age

# A function that belongs to a class is called a method.
# __str__ is a dunder/special method : called automatically by print()
# to represent the object as a string.
    def __str__(self) -> str:
        return f"{self.name}: {self.height}cm, {self.age} days old"


def ft_garden_data() -> None:
    print("=== Garden Plant Registry ===")
    my_plants: list[Plant] = [
        Plant("Rose", 25, 30),
        Plant("Sunflower", 80, 45),
        Plant("Cactus", 15, 120),
    ]
    for plant in my_plants:
        print(plant)


if __name__ == "__main__":
    ft_garden_data()
