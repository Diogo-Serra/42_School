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


def _battle_type_label(creature):
    creature_type = creature.creature_type
    return creature_type[0].upper() + creature_type[1:]


def _strategy_name(strategy):
    if isinstance(strategy, NormalStrategy):
        return "Normal"
    if isinstance(strategy, AggressiveStrategy):
        return "Aggressive"
    return "Defensive"


def _opponent_name(factory):
    creature = factory.create_base()
    if creature.name == "Sproutling":
        return "Healing"
    if creature.name == "Shiftling":
        return "Transform"
    return creature.name


def print_opponents(opponents):
    entries = []
    for factory, strategy in opponents:
        factory_name = _opponent_name(factory)
        strategy_name = _strategy_name(strategy)
        opponent_entry = f"({factory_name}+{strategy_name})"
        entries.append(opponent_entry)
    print(f"[ {', '.join(entries)} ]")


def print_battle(opponent1, opponent2):
    factory1, strategy1 = opponent1
    factory2, strategy2 = opponent2

    creature1 = factory1.create_base()
    creature2 = factory2.create_base()
    creature1_line = f"{creature1.name} is a {_battle_type_label(creature1)}"
    creature2_line = f"{creature2.name} is a {_battle_type_label(creature2)}"

    print("\n* Battle *")
    print(f"{creature1_line} type Creature")
    print("vs.")
    print(f"{creature2_line} type Creature")
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
                print_battle(opponents[i], opponents[j])
    except InvalidStrategyCreatureError as error:
        print(f"Battle error, aborting tournament: {error}")


def print_tournament(title, opponents):
    print(title)
    print_opponents(opponents)
    battle(opponents)


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
    print_tournament("\nTournament 0 (basic)", opponents_0)

    opponents_1 = [
        (flame_factory, aggressive_strategy),
        (healing_factory, defensive_strategy),
    ]
    print_tournament("\nTournament 1 (error)", opponents_1)

    opponents_2 = [
        (aqua_factory, normal_strategy),
        (healing_factory, defensive_strategy),
        (transform_factory, aggressive_strategy),
    ]
    print_tournament("\nTournament 2 (multiple)", opponents_2)


if __name__ == "__main__":
    main()
