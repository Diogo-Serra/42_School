from ..ex0 import Creature
from .Capabilities import HealCapability as Heal


class Sproutling(Creature, Heal):

    def __init__(self):
        self.name = "Sproutling"
        self.type = "Grass"
        self.attack = "Vine Whip"

    def attack(self):
        return f"{self.name} uses Vine Whip"


class Bloomelle(Creature, Heal):

    def attack(self):
        return f"{self.name} uses Petal Dance"
