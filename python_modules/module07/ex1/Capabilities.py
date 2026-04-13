from abc import ABC, abstractmethod
from ex0.Creature import Creature


class HealCapability(ABC):

    @abstractmethod
    def heal(self, target: Creature) -> str:
        ...


class TransformCapability(ABC):
    def __init__(self) -> None:
        self.status = "base"

    @abstractmethod
    def transform(self) -> str:
        ...

    @abstractmethod
    def revert(self) -> str:
        ...
