#!/usr/bin/env python3
import random


achievements: set = {
        'boss_slayer',
        'collector',
        'first_kill',
        'level_10',
        'perfectionist',
        'speed_demon',
        'treasure_hunter'}


class Player:

    def __init__(self, name: str):
        self.name = name
        self.achievements = gen_player_achievements()

    def __str__(self):
        return f"Player {self.name}: Achievements: {self.achievements}"


def gen_player_achievements() -> set:
    player_achievement: set = set()

    count = random.randint(1, 6)
    for i in range(count):
        player_achievement.add(random.choice(tuple(achievements)))
    return player_achievement


def main():

    print("=== Achievement Tracker System ===\n")
    players_list: list[Player] = [
        Player("Alice"),
        Player("Bob"),
        Player("Charlie"),
        Player("Dylan")]

    for player in players_list:
        print(player)
        print()

    alice, bob, charlie, dylan = players_list
    a_set = alice.achievements
    b_set = bob.achievements
    c_set = charlie.achievements
    d_set = dylan.achievements

    common = a_set & b_set & c_set & d_set
    print(f"Common achievements: {common}")
    print()
    print(f"Only Alice has: {a_set - (b_set | c_set | d_set)}")
    print(f"Only Bob has: {b_set - (a_set | c_set | d_set)}")
    print(f"Only Charlie has: {c_set - (a_set | b_set | d_set)}")
    print(f"Only Dylan has: {d_set - (a_set | b_set | c_set)}")
    print()
    print(f"Alice is missing: {achievements - a_set}")
    print(f"Bob is missing: {achievements - b_set}")
    print(f"Charlie is missing: {achievements - c_set}")
    print(f"Dylan is missing: {achievements - d_set}")


main()


"""
def ft_achievement_tracker(players: list[set]):
    achievements: set = {
        'boss_slayer',
        'collector',
        'first_kill',
        'level_10',
        'perfectionist',
        'speed_demon',
        'treasure_hunter'}
    a, b, c = players[0], players[1], players[2]
    print("\n=== Achievement Analytics ===")
    print(f"All unique achievements: {achievements}")
    print(f"Total unique achievements: {len(achievements)}")
    common_toall: set = a & b & c
    print(f"\nCommon to all players: {common_toall}")
    rare_achiev: set = ((a - b - c) | (b - a - c) | (c - a - b)) & achievements
    print(f"Rare achievements (1 player): {rare_achiev}\n")
    a_b = a & b
    print(f"Alice vs Bob common: {a_b}")
    a_unique: set = a - b
    print(f"Alice unique: {a_unique}")
    b_unique: set = b - a
    print(f"Bob unique: {b_unique}")
"""
