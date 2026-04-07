from abc import ABC, abstractmethod


class Creature(ABC):

    @abstractmethod
    def attack(self):
        ...

    def describe(self):
        return f"{self.name} is a {self.creature_type} type Creature"


class Flameling(Creature):
    def __init__(self) -> None:
        self.name = "Flameling"
        self.creature_type = "fire"
        self.attack = "Ember"

    def attack(self):
        return f"{self.name} uses {self.attack}"


class Pyrodon(Creature):
    def __init__(self) -> None:
        self.name = "Pyrodon"
        self.creature_type = "fire"
        self.attack = "Flamethrower"

    def attack(self):
        return f"{self.name} uses {self.attack}"


class Aquabub(Creature):
    def __init__(self) -> None:
        self.name = "Aquabub"
        self.creature_type = "water"
        self.attack = "Water Gun"

    def attack(self):
        return f"{self.name} uses {self.attack}"


class Torragon(Creature):
    def __init__(self) -> None:
        self.name = "Torragon"
        self.creature_type = "water"
        self.attack = "Hydro Pump"

    def attack(self):
        return f"{self.name} uses {self.attack}"
