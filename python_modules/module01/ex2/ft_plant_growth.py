#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age
        self.initial_heigh = height
        self.day = 1

    def grow(self) -> None:
        self.height += 1

    def mature(self) -> None:
        self.age += 1
        self.day += 1

    def get_info(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.age} days old")
        print(f"Growth this week: +{self.height - self.initial_heigh}cm")


def ft_plant_growth() -> None:
    my_plants: list[Plant] = [
        Plant("Rose", 25, 30),
        Plant("Sunflower", 80, 45),
        Plant("Cactus", 15, 120),
    ]
    day = 1
    print(f"=== Day {day} ===")
    for plant in my_plants:
        plant.get_info()
    for i in range(6):
        for plant in my_plants:
            plant.grow()
            plant.mature()
        day += 1
    print(f"=== Day {day} ===")
    for plant in my_plants:
        plant.get_info()


if __name__ == "__main__":
    ft_plant_growth()
