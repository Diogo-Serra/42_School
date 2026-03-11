#!/usr/bin/env python3

# __ (double underscore) makes an attribute private via name mangling
# encapsulation so data is only changed through controlled methods.
class SecurePlant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        print(self)
        self.height = height
        self.age = age

    # @property + @x.setter
    # route attribute access through getter/setter methods.
    @property
    def height(self) -> int:
        return self.__height

    @height.setter
    def height(self, value: int) -> None:
        if value < 0:
            print(f"Invalid operation attempted: height {value} [REJECTED]")
            print("Security: Negative height rejected\n")
        else:
            self.__height = value
            print(f"Height updated: {value}cm [OK]")

    @property
    def age(self) -> int:
        return self.__age

    @age.setter
    def age(self, value: int) -> None:
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
        plant.height = -5
    print(f"Current plant: {plant.name} "
          f"({plant.height}cm, {plant.age} days)")


if __name__ == "__main__":
    ft_garden_security()
