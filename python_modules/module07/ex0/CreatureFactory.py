from abc import ABC, abstractmethod


class CreatureFactory(ABC):

    @abstractmethod
    def create_base(self):
        ...

    @abstractmethod
    def create_evolved(self):
        ...


class FlameFactory(CreatureFactory):

    def create_base(self):
        from .Creature import Flameling
        return Flameling()

    def create_evolved(self):
        from .Creature import Pyrodon
        return Pyrodon()


class AquaFactory(CreatureFactory):
    def create_base(self):
        from .Creature import Aquabub
        return Aquabub()

    def create_evolved(self):
        from .Creature import Torragon
        return Torragon()
