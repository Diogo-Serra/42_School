from typing import Callable
from abc import ABC, abstractmethod
from ex1.Capabilities import HealCapability, TransformCapability


class InvalidStrategyCreatureError(Exception):
    pass


class BattleStrategy(ABC):

    @abstractmethod
    def act(self, creature: list[tuple]) -> (InvalidStrategyCreatureError |
                                             list[Callable]):
        ...

    @abstractmethod
    def is_valid(self, creature: list[tuple]) -> bool:
        ...


def _format_action(action: str) -> str:
    if action.endswith(("!", ".", "?")):
        return action
    return f"{action}!"


class NormalStrategy(BattleStrategy):

    def is_valid(self, creature):
        return hasattr(creature, "attack")

    def act(self, creature):
        if not self.is_valid(creature):
            raise InvalidStrategyCreatureError(
                f"Invalid Creature '{creature.name}' for this normal strategy"
            )
        return [_format_action(creature.attack())]


class AggressiveStrategy(BattleStrategy):

    def is_valid(self, creature):
        return isinstance(creature, TransformCapability)

    def act(self, creature):
        if not self.is_valid(creature):
            raise InvalidStrategyCreatureError(
                f"Invalid Creature '{creature.name}' "
                "for this aggressive strategy"
            )
        return [
            creature.transform(),
            _format_action(creature.attack()),
            creature.revert(),
        ]


class DefensiveStrategy(BattleStrategy):

    def is_valid(self, creature):
        return isinstance(creature, HealCapability)

    def act(self, creature):
        if not self.is_valid(creature):
            raise InvalidStrategyCreatureError(
                f"Invalid Creature '{creature.name}' "
                "for this defensive strategy"
            )
        return [_format_action(creature.attack()), creature.heal()]
