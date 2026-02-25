#!/usr/bin/env python3

class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age


def print_plant(Plants):
    for Plant in Plants:
        print(f"{Plant.name}: {Plant.height}cm, {Plant.age} days old")


def ft_garden_data():
    print("=== Garden Plant Registry ===")
    My_Plants = [
        Plant("Rose", 25, 30),
        Plant("Sunflower", 80, 45),
        Plant("Cactus", 15, 120)]
    print_plant(My_Plants)


if __name__ == "__main__":
    ft_garden_data()
