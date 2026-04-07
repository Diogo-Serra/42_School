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

    def attack(self):
        return f"{self.name} uses Ember"


class Pyrodon(Creature):
    def __init__(self) -> None:
        self.name = "Pyrodon"
        self.creature_type = "fire"

    def attack(self):
        return f"{self.name} uses Flamethrower"


class Aquabub(Creature):
    def __init__(self) -> None:
        self.name = "Aquabub"
        self.creature_type = "water"

    def attack(self):
        return f"{self.name} uses Water Gun"


class Torragon(Creature):
    def __init__(self) -> None:
        self.name = "Torragon"
        self.creature_type = "water"

    def attack(self):
        return f"{self.name} uses Hydro Pump"
