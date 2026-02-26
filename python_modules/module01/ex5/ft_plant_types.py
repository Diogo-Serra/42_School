#!/usr/bin/env python3

class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age


class Tree(Plant):
    def __init__(self, name, height, age, trunk_diameter):
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self):
        print(f"{self.name} provides 78 square"
              f" meters of shade\n")


class Flower(Plant):
    def __init__(self, name, height, age, color):
        super().__init__(name, height, age)
        self.color = color

    def bloom(self):
        print(f"{self.name} is blooming beautifully!\n")


class Vegetable(Plant):
    def __init__(self, name, height, age, harvest_season, nutritional_value):
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value


def ft_plant_types():
    my_flowers = [
        Flower("Rose", 25, 30, "red"),
        Flower("Tulip", 15, 20, "yellow")]
    my_trees = [
        Tree("Oak", 500, 1825, 50),
        Tree("Birch", 550, 1755, 30)]
    my_vegetables = [
        Vegetable("Tomato", 80, 90, "summer harvest", "vitamin C"),
        Vegetable("Carrot", 15, 30, "spring harvest", "vitamin C")
    ]
    print("=== Garden Plant Types ===\n")
    print(f"{my_flowers[0].name} ({type(my_flowers[0]).__name__}): "
          f"{my_flowers[0].height}cm, {my_flowers[0].age} days, "
          f"{my_flowers[0].color} color")
    Flower.bloom(my_flowers[0])
    print(f"{my_trees[0].name} ({type(my_trees[0]).__name__}): "
          f"{my_trees[0].height}cm, {my_trees[0].age} days, "
          f"{my_trees[0].trunk_diameter}cm diameter")
    Tree.produce_shade(my_trees[0])
    print(f"{my_vegetables[0].name} ({type(my_vegetables[0]).__name__}): "
          f"{my_vegetables[0].height}cm, {my_vegetables[0].age} days, "
          f"{my_vegetables[0].harvest_season}")
    print(f"{my_vegetables[0].name} is rich in "
          f"{my_vegetables[0].nutritional_value}")


ft_plant_types()
