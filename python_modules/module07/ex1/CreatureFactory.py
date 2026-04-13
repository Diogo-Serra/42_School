from .Creature import Shiftling, Sproutling, Morphagon, Bloomelle
from ex0.CreatureFactory import CreatureFactory


class TransformCreatureFactory(CreatureFactory):
    def create_base(self):
        return Shiftling()

    def create_evolved(self):
        return Morphagon()


class HealingCreatureFactory(CreatureFactory):

    def create_base(self):
        return Sproutling()

    def create_evolved(self):
        return Bloomelle()
