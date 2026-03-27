#!/usr/bin/env python3
import random


achievements: list[str] = [
        'boss_slayer',
        'collector',
        'first_kill',
        'level_10',
        'perfectionist',
        'speed_demon',
        'treasure_hunter']


class Player:

    def __init__(self, name: str) -> None:
        self.name = name
        self.achievements: set = gen_player_achievements()

    def __str__(self) -> str:
        return f"Player {self.name}: Achievements: {self.achievements}"


def gen_player_achievements() -> set[str]:
    player_achievement: set = set()

    count: int = random.randint(4, 6)
    for i in range(count):
        player_achievement.add(random.choice(tuple(achievements)))
    return set(player_achievement)


def main() -> None:

    print("=== Achievement Tracker System ===\n")
    players_list: list[Player] = [
        Player("Alice"),
        Player("Bob"),
        Player("Charlie"),
        Player("Dylan")]

    for player in players_list:
        print(player)
        print()

    alice: Player
    bob: Player
    charlie: Player
    dylan: Player
    alice, bob, charlie, dylan = players_list
    a_set: set = alice.achievements
    b_set: set = bob.achievements
    c_set: set = charlie.achievements
    d_set: set = dylan.achievements

    common: set = a_set & b_set & c_set & d_set
    print(f"Common achievements: {common}")
    print()
    print(f"Only Alice has: {a_set - (b_set | c_set | d_set)}")
    print(f"Only Bob has: {b_set - (a_set | c_set | d_set)}")
    print(f"Only Charlie has: {c_set - (a_set | b_set | d_set)}")
    print(f"Only Dylan has: {d_set - (a_set | b_set | c_set)}")
    print()
    print(f"Alice is missing: {set(achievements) - a_set}")
    print(f"Bob is missing: {set(achievements) - b_set}")
    print(f"Charlie is missing: {set(achievements) - c_set}")
    print(f"Dylan is missing: {set(achievements) - d_set}")


main()
