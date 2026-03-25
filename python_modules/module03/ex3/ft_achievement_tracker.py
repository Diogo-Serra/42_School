#!/usr/bin/env python3
import random


def gen_player_achievements() -> set:
    player_achievement: set = set()
    achievements: set = {
        'boss_slayer',
        'collector',
        'first_kill',
        'level_10',
        'perfectionist',
        'speed_demon',
        'treasure_hunter'}

    for i in range(1, 6):
        player_achievement.add(random.choice(tuple(achievements)))
    return player_achievement


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


def main():
    print("=== Achievement Tracker System ===\n")
    alice = gen_player_achievements()
    print(alice)
        

main()
