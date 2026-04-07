from ex0.Creature import Creature
from .ex0.CreatureFactory import CreatureFactory
from .Capabilities import HealCapability as Heal


class HealingCreatureFactory(CreatureFactory):

    def create_base(self):
        return Sproutling()

    def create_evolved(self):
        return Bloomelle()

    def __str__(self):
        return "Heal Factory"


class Sproutling(Creature, Heal):

    def __init__(self):
        self.name = "Sproutling"
        self.type = "Grass"
        self.attack = "Vine Whip"

    def attack(self):
        return f"{self.name} uses {self.attack}"

    def heal(self):
        return f"{self.name} heals itself for a small amount"


class Bloomelle(Creature, Heal):

    def __init__(self):
        self.name = "Bloomelle"
        self.type = "Grass/Fairy"
        self.attack = "Petal Dance"

    def attack(self):
        return f"{self.name} uses {self.attack}"

    def heal(self):
        return f"{self.name} heals itself and others for a large amount"
