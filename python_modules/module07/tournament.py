#!/usr/bin/env python3
from ex0.CreatureFactory import AquaFactory, FlameFactory, CreatureFactory
from ex2.strategy import BattleStrategy, InvalidStrategyCreatureError

from ex1.CreatureFactory import (
    HealingCreatureFactory,
    TransformCreatureFactory)

from ex2.strategies import (
    AggressiveStrategy,
    DefensiveStrategy,
    NormalStrategy)


aqua_factory = AquaFactory()
flame_factory = FlameFactory()
healing_factory = HealingCreatureFactory()
transform_factory = TransformCreatureFactory()

normal_strategy = NormalStrategy()
agressive_strategy = AggressiveStrategy()
defensive_strategy = DefensiveStrategy()

tournament_list = [
    (flame_factory, normal_strategy),
    (healing_factory, defensive_strategy),
    (flame_factory, agressive_strategy),
    (healing_factory, defensive_strategy),
    (aqua_factory, )]


def tournament(opponents:
               list[tuple[CreatureFactory, BattleStrategy]]) -> None:
    print("*** Tournament ***")
    print(f"{len(opponents)} opponents involved")
    fighters = [(factory.create_base(), strategy)
                for factory, strategy in opponents]
    try:
        for i in range(len(fighters)):
            for j in range(i + 1, len(fighters)):
                creature_a, strategy_a = fighters[i]
                creature_b, strategy_b = fighters[j]
                print("* Battle *")
                print(creature_a.describe())
                print("vs.")
                print(creature_b.describe())
                print("now fight!")
                for creature, strategy in [(creature_a, strategy_a),
                                           (creature_b, strategy_b)]:
                    for line in strategy.act(creature):
                        print(line)
    except InvalidStrategyCreatureError as e:
        print(f"Battle error, aborting tournament: {e}")


if __name__ == "__main__":
    tournament([
        (flame_factory, normal_strategy),
        (healing_factory, defensive_strategy),
    ])
    print()
    tournament([
        (flame_factory, agressive_strategy),
        (healing_factory, defensive_strategy),
    ])
    print()
    tournament([
        (aqua_factory, normal_strategy),
        (healing_factory, defensive_strategy),
        (transform_factory, agressive_strategy),
    ])
