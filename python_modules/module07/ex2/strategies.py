from ex0.Creature import Creature
from ex1.Capabilities import HealCapability, TransformCapability
from .strategy import BattleStrategy, InvalidStrategyCreatureError


class NormalStrategy(BattleStrategy):

    def is_valid(self, creature: Creature) -> bool:
        return True

    def act(self, creature: Creature) -> list[str]:
        return [creature.attack()]


class AggressiveStrategy(BattleStrategy):

    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, TransformCapability)

    def act(self, creature: Creature) -> list[str]:
        if not self.is_valid(creature):
            raise InvalidStrategyCreatureError(
                f"Invalid Creature '{creature.name}' "
                "for this aggressive strategy")
        assert isinstance(creature, TransformCapability)
        return [creature.transform(), creature.attack(), creature.revert()]


class DefensiveStrategy(BattleStrategy):

    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, HealCapability)

    def act(self, creature: Creature) -> list[str]:
        if not self.is_valid(creature):
            raise InvalidStrategyCreatureError(
                f"Invalid Creature '{creature.name}' "
                "for this defensive strategy")
        assert isinstance(creature, HealCapability)
        return [creature.attack(), creature.heal()]
