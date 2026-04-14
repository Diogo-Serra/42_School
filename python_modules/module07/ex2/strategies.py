from ex0.Creature import Creature
from typing import Protocol
from ex1.Capabilities import HealCapability, TransformCapability
from .strategy import BattleStrategy, InvalidStrategyCreatureError


class HealerCreature(Protocol):
    name: str

    def attack(self) -> str:
        ...

    def heal(self, target: Creature | None = None) -> str:
        ...


class TransformingCreature(Protocol):
    name: str

    def attack(self) -> str:
        ...

    def transform(self) -> str:
        ...

    def revert(self) -> str:
        ...


class NormalStrategy(BattleStrategy):

    def is_valid(self, creature: Creature) -> bool:
        return hasattr(creature, "attack")

    def act(self, creature: Creature) -> list[str]:
        return [creature.attack()]


class AggressiveStrategy(BattleStrategy):

    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, TransformCapability)

    def act(self, creature: TransformingCreature) -> list[str]:
        if not self.is_valid(creature):
            raise InvalidStrategyCreatureError(
                f"Invalid Creature '{creature.name}' "
                "for this aggressive strategy")
        return [creature.transform(), creature.attack(), creature.revert()]


class DefensiveStrategy(BattleStrategy):

    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, HealCapability)

    def act(self, creature: HealerCreature) -> list[str]:
        if not self.is_valid(creature):
            raise InvalidStrategyCreatureError(
                f"Invalid Creature '{creature.name}' "
                "for this defensive strategy")
        return [creature.attack(), creature.heal()]
