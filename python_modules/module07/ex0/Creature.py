from abc import ABC, abstractmethod


class Creature(ABC):
    def __init__(self, name: str, creature_type: str) -> None:
        self.name = name
        self.creature_type = creature_type

    @abstractmethod
    def attack(self) -> str:
        ...

    def describe(self) -> str:
        return f"{self.name} is a {self.creature_type} type Creature"


class Flameling(Creature):
    def __init__(self, name: str = "Flameling",
                 creature_type: str = "Fire") -> None:
        super().__init__(name, creature_type)
        self.name = name
        self.creature_type = creature_type
        self.basic = "Ember"

    def attack(self) -> str:
        return f"{self.name} uses {self.basic}!"


class Pyrodon(Creature):
    def __init__(self, name: str = "Pyrodon",
                 creature_type: str = "Fire/Flying") -> None:
        super().__init__(name, creature_type)
        self.name = name
        self.creature_type = creature_type
        self.basic = "Flamethrower"

    def attack(self) -> str:
        return f"{self.name} uses {self.basic}!"


class Aquabub(Creature):
    def __init__(self, name: str = "Aquabub",
                 creature_type: str = "Water") -> None:
        super().__init__(name, creature_type)
        self.name = name
        self.creature_type = creature_type
        self.basic = "Water Gun"

    def attack(self) -> str:
        return f"{self.name} uses {self.basic}!"


class Torragon(Creature):
    def __init__(self, name: str = "Torragon",
                 creature_type: str = "Water") -> None:
        super().__init__(name, creature_type)
        self.name = name
        self.creature_type = creature_type
        self.basic = "Hydro Pump"

    def attack(self) -> str:
        return f"{self.name} uses {self.basic}!"
