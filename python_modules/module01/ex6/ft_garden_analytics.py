#!/usr/bin/env python3

class GardenManager:
    def __init__(self, owner):
        self.owner = owner
        self.plants = []

    def welcome_message():
        print("=== Garden Management System Demo ===\n")

    def add_plant(self, plant):
        self.plants.append(plant)

    class GardenStats():
        def __init__(self, owner):
            super().__init__(owner)


class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age


class Tree(Plant):
    def __init__(self, name, height, age):
        super().__init__(name, height, age)


class Flower(Plant):
    def __init__(self, name, height, age):
        super().__init__(name, height, age)


class Vegetable(Plant):
    def __init__(self, name, height, age):
        super().__init__(name, height, age)


def ft_garden_analytics():
    print("Good to go!")


ft_garden_analytics()
