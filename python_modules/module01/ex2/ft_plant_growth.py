#!/usr/bin/env python3

class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age


def grow(Plant) -> None:
    Plant.height += 1


def age(Plant) -> None:
    Plant.age += 1


def get_info(Plant, day) -> None:
    print(f"=== Day {day} ===")
    print(f"{Plant.name}: {Plant.height}cm, {Plant.age} days old")


def ft_plant_growth() -> None:
    day: int = 1
    growth: int = 0
    rose: Plant = Plant("Rose", 25, 30)
    while day <= 7:
        get_info(rose, day)
        grow(rose)
        growth += 1
        age(rose)
        day += 1
    print(f"Growth this week: +{growth - 1}cm")


if __name__ == "__main__":
    ft_plant_growth()
