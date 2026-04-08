#!/usr/bin/env python3
from ex0.CreatureFactory import AquaFactory, FlameFactory
from ex1.CreatureFactory import (
    HealingCreatureFactory,
    TransformCreatureFactory,
)
from ex2.strategy import (
    AggressiveStrategy,
    DefensiveStrategy,
    InvalidStrategyCreatureError,
    NormalStrategy,
)


def _capitalize_creature_type(creature_type: str) -> str:
    if not creature_type:
        return creature_type
    return creature_type[0].upper() + creature_type[1:]


def _strategy_label(strategy) -> str:
    if isinstance(strategy, NormalStrategy):
        return "Normal"
    if isinstance(strategy, AggressiveStrategy):
        return "Aggressive"
    return "Defensive"


def _factory_label(factory) -> str:
    creature = factory.create_base()
    if creature.name == "Sproutling":
        return "Healing"
    if creature.name == "Shiftling":
        return "Transform"
    return creature.name


def _print_opponents(opponents):
    entries = []
    for factory, strategy in opponents:
        factory_name = _factory_label(factory)
        strategy_name = _strategy_label(strategy)
        opponent_entry = f"({factory_name}+{strategy_name})"
        entries.append(opponent_entry)
    print(f"[ {', '.join(entries)} ]")


def _fight(opponent1, opponent2):
    factory1, strategy1 = opponent1
    factory2, strategy2 = opponent2

    creature1 = factory1.create_base()
    creature2 = factory2.create_base()

    print("* Battle *")
    print(
        f"{creature1.name} is a "
        f"{_capitalize_creature_type(creature1.creature_type)} type Creature"
    )
    print("vs.")
    print(
        f"{creature2.name} is a "
        f"{_capitalize_creature_type(creature2.creature_type)} type Creature"
    )
    print("now fight!")

    for action in strategy1.act(creature1):
        print(action)
    for action in strategy2.act(creature2):
        print(action)


def battle(opponents):
    print("*** Tournament ***")
    print(f"{len(opponents)} opponents involved")

    try:
        for i in range(len(opponents)):
            for j in range(i + 1, len(opponents)):
                _fight(opponents[i], opponents[j])
    except InvalidStrategyCreatureError as error:
        print(f"Battle error, aborting tournament: {error}")


def main():
    flame_factory = FlameFactory()
    aqua_factory = AquaFactory()
    healing_factory = HealingCreatureFactory()
    transform_factory = TransformCreatureFactory()

    normal_strategy = NormalStrategy()
    aggressive_strategy = AggressiveStrategy()
    defensive_strategy = DefensiveStrategy()

    opponents_0 = [
        (flame_factory, normal_strategy),
        (healing_factory, defensive_strategy),
    ]
    print("Tournament 0 (basic)")
    _print_opponents(opponents_0)
    battle(opponents_0)

    opponents_1 = [
        (flame_factory, aggressive_strategy),
        (healing_factory, defensive_strategy),
    ]
    print("Tournament 1 (error)")
    _print_opponents(opponents_1)
    battle(opponents_1)

    opponents_2 = [
        (aqua_factory, normal_strategy),
        (healing_factory, defensive_strategy),
        (transform_factory, aggressive_strategy),
    ]
    print("Tournament 2 (multiple)")
    _print_opponents(opponents_2)
    battle(opponents_2)


if __name__ == "__main__":
    main()
