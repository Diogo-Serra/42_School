from abc import ABC, abstractmethod
from .Creature import Flameling, Pyrodon, Aquabub, Torragon


class CreatureFactory(ABC):

    @abstractmethod
    def create_base(self):
        ...

    @abstractmethod
    def create_evolved(self):
        ...


class FlameFactory(CreatureFactory):

    def create_base(self):
        return Flameling()

    def create_evolved(self):
        return Pyrodon()


class AquaFactory(CreatureFactory):
    def create_base(self):
        return Aquabub()

    def create_evolved(self):
        return Torragon()
