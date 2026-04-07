from abc import ABC, abstractmethod


class Creature(ABC):

    @abstractmethod
    def attack(self):
        ...

    def describe(self):
        return f"{self.name}: {self.creature_type}"


class Flameling(Creature):
    def __init__(self) -> None:
        self.name = "Flameling"
        self.creature_type = "fire"

    def attack(self):
        return "Ember"


class Pyrodon(Creature):
    def __init__(self) -> None:
        self.name = "Pyrodon"
        self.creature_type = "fire"

    def attack(self):
        return "Flamethrower"


class Aquabub(Creature):
    def __init__(self) -> None:
        self.name = "Aquabub"
        self.creature_type = "water"

    def attack(self):
        return "Water Gun"


class Torragon(Creature):
    def __init__(self) -> None:
        self.name = "Torragon"
        self.creature_type = "water"

    def attack(self):
        return "Hydro Pump"
