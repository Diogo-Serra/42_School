#!/usr/bin/env python3

class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age

    def grow_1_cm(self) -> None:
        self.height += 1

    def age_1_day(self) -> None:
        self.age += 1

    def get_info(self, day) -> None:
        print(f"=== Day {day} ===")
        print(f"{self.name}: {self.height}cm, {self.age} days old")


def ft_plant_growth() -> None:
    plants = [
        Plant("Rose", 25, 30)]
    for plant in plants:
        initial_height: int = plant.height
        for day in range(1, 8):
            plant.get_info(day)
            plant.grow_1_cm()
            plant.age_1_day()
    print(f"Growth this week: +{plant.height - initial_height - 1}cm")


if __name__ == "__main__":
    ft_plant_growth()
