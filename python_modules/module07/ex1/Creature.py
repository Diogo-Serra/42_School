from ex0.Creature import Creature
from .Capabilities import TransformCapability as Transform
from .Capabilities import HealCapability as Heal


class Sproutling(Creature, Heal):

    def __init__(self, name: str = "Sproutling",
                 creature_type: str = "Grass") -> None:
        super().__init__(name, creature_type)
        self.name = name
        self.creature_type = creature_type
        self.basic = "Vine Whip"

    def attack(self) -> str:
        return f"{self.name} uses {self.basic}"

    def heal(self) -> str:
        return f"{self.name} heals itself for a small amount"


class Bloomelle(Creature, Heal):

    def __init__(self, name: str = "Bloomelle",
                 creature_type: str = "Grass/Fairy") -> None:
        self.name = name
        self.creature_type = creature_type
        self.basic = "Petal Dance"

    def attack(self) -> str:
        return f"{self.name} uses {self.basic}."

    def heal(self) -> str:
        return f"{self.name} heals itself and others for a large amount."


class Shiftling(Creature, Transform):

    def __init__(self, name: str = "Shiftling",
                 creature_type: str = "Normal") -> None:
        self.name = name
        self.creature_type = creature_type

    def attack(self) -> str:
        if self.status == "normal":
            return f"{self.name} attacks normally."
        else:
            return f"{self.name} performs a boosted strike!"

    def transform(self) -> str:
        self.status = "transformed"
        return f"{self.name} shifts into a sharper form!"

    def revert(self) -> str:
        self.status = "normal"
        return f"{self.name} returns to normal."


class Morphagon(Creature, Transform):

    def __init__(self, name: str, creature_type: str) -> None:
        self.name = name
        self.creature_type = creature_type

    def attack(self) -> str:
        if self.status == "normal":
            return f"{self.name} attacks normally."
        else:
            return f"{self.name} unleashes a devastating morph strike!"

    def transform(self) -> str:
        self.status = "transformed"
        return f"{self.name} morphs into a dragonic battle form!"

    def revert(self) -> str:
        self.status = "normal"
        return f"{self.name} stabilizes its form."
