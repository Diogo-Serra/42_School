#!/usr/bin/env python3

class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age

    def __str__(self) -> str:
        return f"Created: {self.name}: ({self.height}cm, {self.age} days)"


def ft_plant_factory() -> None:
    plant_data = [
        ("Rose", 25, 30),
        ("Oak", 200, 365),
        ("Cactus", 5, 90),
        ("Sunflower", 80, 45),
        ("Fern", 15, 120)
    ]
    my_plants = [Plant(name, height, age) for name, height, age in plant_data]
    print("=== Plant Factory Output ===")
    for plants in my_plants:
        print(plants)
    print(f"\nTotal plants created: {len(my_plants)}")


if __name__ == "__main__":
    ft_plant_factory()
