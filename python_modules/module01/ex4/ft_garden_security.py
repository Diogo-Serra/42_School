#!/usr/bin/env python3

class SecurePlant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.__height = 0
        self.__age = 0
        print(self)
        self.set_height(height)
        self.set_age(age)

    def get_height(self) -> int:
        return self.__height

    def get_age(self) -> int:
        return self.__age

    def set_height(self, value: int) -> None:
        if value < 0:
            print(f"Invalid operation attempted: height {value} [REJECTED]")
            print("Security: Negative height rejected\n")
        else:
            self.__height = value
            print(f"Height updated: {value}cm [OK]")

    def set_age(self, value: int) -> None:
        if value < 0:
            print(f"Invalid operation attempted: age {value} [REJECTED]")
            print("Security: Negative age rejected\n")
        else:
            self.__age = value
            print(f"Age updated: {value} days [OK]\n")

    def __str__(self):
        return f"Plant created: {self.name}"


def ft_garden_security() -> None:
    print("=== Garden Security System ===")
    my_plants = [
        SecurePlant("Rose", 25, 30)]
    for plant in my_plants:
        plant.set_height(-5)
    print(f"Current plant: {plant.name} "
          f"{plant.get_height()}cm, {plant.get_age()} days")


if __name__ == "__main__":
    ft_garden_security()
