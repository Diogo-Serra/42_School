#!/usr/bin/env python3
import math


class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age


class Tree(Plant):
    def __init__(self, name: str, height: int, age: int,
                 trunk_diameter: int) -> None:
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter
        print(self)
        self.produce_shade()

    def __str__(self) -> str:
        return (f"\n{self.name} ({type(self).__name__}): "
                f"{self.height}cm, {self.age} days, "
                f"{self.trunk_diameter}cm diameter")

    def produce_shade(self) -> None:
        self.shade: int = int(math.pi * (self.trunk_diameter / 10) ** 2)
        print(f"{self.name} provides {self.shade} square"
              f" meters of shade")


class Flower(Plant):
    def __init__(self, name: str, height: int, age: int, color: str) -> None:
        super().__init__(name, height, age)
        self.color = color
        print(self)
        self.bloom()

    def __str__(self) -> str:
        return (f"\n{self.name} ({type(self).__name__}): "
                f"{self.height}cm, {self.age} days, "
                f"{self.color} color")

    def bloom(self) -> None:
        print(f"{self.name} is blooming beautifully!")


class Vegetable(Plant):
    def __init__(self, name: str, height: int, age: int, harvest_season: str,
                 nutritional_value: str) -> None:
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value
        print(self)
        self.info_vegetable()

    def __str__(self) -> str:
        return (f"\n{self.name} ({type(self).__name__}): "
                f"{self.height}cm, {self.age} days, "
                f"{self.harvest_season}")

    def info_vegetable(self) -> None:
        print(f"{self.name} is rich in {self.nutritional_value}")


def ft_plant_types():
    print("=== Garden Plant Types ===\n")
    print("= Flowers =")
    my_flowers: list[Plant[Flower]] = [ # noqa
        Flower("Rose", 25, 30, "red"),
        Flower("Tulip", 15, 20, "yellow")]
    print("\n= Trees =")
    my_trees: list[Plant[Tree]] = [ # noqa
        Tree("Oak", 500, 1825, 50),
        Tree("Birch", 550, 1755, 30)]
    print("\n= Vegetables =")
    my_vegetables: list[Plant[Vegetable]] = [ # noqa
        Vegetable("Tomato", 80, 90, "summer harvest", "vitamin C"),
        Vegetable("Carrot", 15, 30, "spring harvest", "vitamin C")]


if __name__ == '__main__':
    ft_plant_types()
