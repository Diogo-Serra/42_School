from abc import ABC, abstractmethod


class Creature(ABC):
    def __init__(self, name: str, creature_type: str) -> None:
        super().__init__()
        self.name = name
        self.creature_type = creature_type

    @abstractmethod
    def attack(self) -> str:
        ...

    def describe(self) -> str:
        return f"{self.name} is a {self.creature_type} type Creature"

    def __str__(self) -> str:
        return f"{self.name}"


class Flameling(Creature):
    def __init__(self) -> None:
        super().__init__("Flameling", "Fire")
        self.basic = "Ember"

    def attack(self) -> str:
        return f"{self.name} uses {self.basic}!"


class Pyrodon(Creature):
    def __init__(self) -> None:
        super().__init__("Pyrodon", "Fire/Flying")
        self.basic = "Flamethrower"

    def attack(self) -> str:
        return f"{self.name} uses {self.basic}!"


class Aquabub(Creature):
    def __init__(self) -> None:
        super().__init__("Aquabub", "Water")
        self.basic = "Water Gun"

    def attack(self) -> str:
        return f"{self.name} uses {self.basic}!"


class Torragon(Creature):
    def __init__(self) -> None:
        super().__init__("Torragon", "Water")
        self.basic = "Hydro Pump"

    def attack(self) -> str:
        return f"{self.name} uses {self.basic}!"
