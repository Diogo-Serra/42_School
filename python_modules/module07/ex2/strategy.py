from ex0.Creature import Creature
from abc import ABC, abstractmethod


class InvalidStrategyCreatureError(Exception):
    pass


class BattleStrategy(ABC):

    @abstractmethod
    def act(self, creature: Creature) -> list[str]:
        ...

    @abstractmethod
    def is_valid(self, creature: Creature) -> bool:
        ...
