#!/usr/bin/env python3

class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self._height = height
        self._age = age
    
    def get_height(self):
        return self._height
    
    def set_height(self, value):
        if value < 0:
            print(f"Invalid operation attempted: height {value} [REJECTED]")
            print("Security: Negative height rejected")
        else:
            self._height = value
            print(f"Height updated: {value}cm [OK]")

    def get_age(self):
        return self._age
    
    def set_age(self, value):
        if value < 0:
            print(f"Invalid operation attempted: age {value} [REJECTED]")
            print("Security: Negative age rejected")
        else:
            self._age = value
            print(f"Age updated: {value} days [OK]")

    def print_plant(self):
        print(f"Plant created: {self.name}")


def ft_garden_security() -> None:
    plant_data = [
        ("Rose", 25, 30),
    ]
    my_plants = [Plant(name, height, age) for name, height, age in plant_data]
    print("=== Garden Security System ===")
    for plant in my_plants:
        plant.print_plant()
        plant.set_height(30)
        plant.set_age(35)
    print(f"Current plant: {plant.name} ({plant.get_height()}cm, {plant.get_age()} days)")


if __name__ == "__main__":
    ft_garden_security()
