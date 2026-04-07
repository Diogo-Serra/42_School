from ex0.Creature import Creature
from .Capabilities import TransformCapability as Transform
from .Capabilities import HealCapability as Heal


class Sproutling(Creature, Heal):

    def __init__(self):
        self.name = "Sproutling"
        self.creature_type = "Grass"
        self.basic = "Vine Whip"

    def attack(self):
        return f"{self.name} uses {self.basic}"

    def heal(self):
        return f"{self.name} heals itself for a small amount"


class Bloomelle(Creature, Heal):

    def __init__(self):
        self.name = "Bloomelle"
        self.creature_type = "Grass/Fairy"
        self.basic = "Petal Dance"

    def attack(self):
        return f"{self.name} uses {self.basic}."

    def heal(self):
        return f"{self.name} heals itself and others for a large amount."


class Shiftling(Creature, Transform):

    def __init__(self):
        self.name = "Shiftling"
        self.creature_type = "Normal"

    def attack(self):
        if self.status == "normal":
            return f"{self.name} attacks normally."
        else:
            return f"{self.name} performs a boosted strike!"

    def transform(self):
        self.status = "transformed"
        return f"{self.name} shifts into a sharper form!"

    def revert(self):
        self.status = "normal"
        return f"{self.name} returns to normal."


class Morphagon(Creature, Transform):

    def __init__(self):
        self.name = "Morphagon"
        self.creature_type = "Normal/Dragon"

    def attack(self):
        if self.status == "normal":
            return f"{self.name} attacks normally."
        else:
            return f"{self.name} unleashes a devastating morph strike!"

    def transform(self):
        self.status = "transformed"
        return f"{self.name} morphs into a dragonic battle form!"

    def revert(self):
        self.status = "normal"
        return f"{self.name} stabilizes its form."
