#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age
        print(self)

    # Info printing (String representation of Plant object)
    def __str__(self) -> str:
        return f"Created: {self.name}: ({self.height}cm, {self.age} days)"


def ft_plant_factory() -> None:
    # Data for plants
    plant_data: list[tuple] = [
        ("Rose", 25, 30),
        ("Oak", 200, 365),
        ("Cactus", 5, 90),
        ("Sunflower", 80, 45),
        ("Fern", 15, 120)
    ]
    # Creation of list of objects for each plant_data info
    print("=== Plant Factory Output ===")
    my_plants: list[Plant] = [
        Plant(name, height, age) for name, height, age in plant_data]
    print(f"\nTotal plants created: {len(my_plants)}")


if __name__ == "__main__":
    ft_plant_factory()
