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
            print("Error: Height cannot be negative.")
        else:
            self._height = value
    
    def get_age(self):
        return self._age
    
    def set_age(self, value):
        if value < 0:
            print("Error: Age cannot be negative.")
        else:
            self._age = value


def ft_garden_security() -> None:
    plant_data = [
        ("Rose", 25, 30),
    ]
    my_plants = [Plant(name, height, age) for name, height, age in plant_data]
    print("=== Garden Security System ===")



if __name__ == "__main__":
    ft_garden_security()
