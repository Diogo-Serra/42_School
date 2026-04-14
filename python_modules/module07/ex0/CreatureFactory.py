from abc import ABC, abstractmethod
from .Creature import Creature, Flameling, Pyrodon, Aquabub, Torragon


class CreatureFactory(ABC):

    @abstractmethod
    def create_base(self) -> Creature:
        ...

    @abstractmethod
    def create_evolved(self) -> Creature:
        ...


class FlameFactory(CreatureFactory):

    def create_base(self) -> Flameling:
        return Flameling()

    def create_evolved(self) -> Pyrodon:
        return Pyrodon()


class AquaFactory(CreatureFactory):

    def create_base(self) -> Aquabub:
        return Aquabub()

    def create_evolved(self) -> Torragon:
        return Torragon()
