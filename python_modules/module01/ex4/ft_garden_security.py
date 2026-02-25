#!/usr/bin/env python3

class SecurePlant:
    def __init__(self, name, height, age):
        self.name = name
        self.__height = height
        self.__age = age
        self.print_plant()

 
    def get_height(self):
        return self.__height

    def set_height(self, value):
        if value < 0:
            print(f"Invalid operation attempted: height {value} [REJECTED]")
            print("Security: Negative height rejected\n")
        else:
            self.__height = value
            print(f"Height updated: {value}cm [OK]")

    def get_age(self):
        return self.__age

    def set_age(self, value):
        if value < 0:
            print(f"Invalid operation attempted: age {value} [REJECTED]")
            print("Security: Negative age rejected\n")
        else:
            self.__age = value
            print(f"Age updated: {value} days [OK]\n")

    def print_plant(self):
        print(f"Plant created: {self.name}")


def ft_garden_security() -> None:
    print("=== Garden Security System ===")
    my_plants = [SecurePlant("Rose", 0, 0)]
    for plant in my_plants:
        plant.set_height(-5)
    print(f"Current plant: {plant.name} "
          f"{plant.get_height()}cm, {plant.get_age()} days")


if __name__ == "__main__":
    ft_garden_security()
