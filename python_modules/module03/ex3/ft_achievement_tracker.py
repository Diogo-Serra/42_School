#!/usr/bin/env python3

"""
=== Achievement Tracker System ===
Player alice achievements: {'first_kill', 'level_10', 'treasure_hunter', 'speed_demon'}
Player bob achievements: {'first_kill', 'level_10', 'boss_slayer', 'collector'}
Player charlie achievements: {'level_10', 'treasure_hunter', 'boss_slayer', 'speed_demon', '
perfectionist'}
=== Achievement Analytics ===
All unique achievements: {'boss_slayer', 'collector', 'first_kill', 'level_10', 'perfectionist', '
speed_demon', 'treasure_hunter'}
Total unique achievements: 7
Common to all players: {'level_10'}
Rare achievements (1 player): {'collector', 'perfectionist'}
Alice vs Bob common: {'first_kill', 'level_10'}
Alice unique: {'speed_demon', 'treasure_hunter'}
Bob unique: {'boss_slayer', 'collector'}
"""


def ft_achievement_tracker(players: list[set]):
    achievements: set = {
        "first_kill",
        "treasure_hunter",
        "speed_demon",
        "collector",
        "boss_slayer",
        "level_10",
        "perfectionist"}
    a, b, c = players[0], players[1], players[2]
    print("=== Achievement Tracker System ===")
    print(f"All unique achievements: {achievements}")
    print(f"Total unique achievements: {len(achievements)}")
    common_toall: set = a & b & c
    print(f"Common to all players: {common_toall}")
    rare_achiev: set = ((a - b - c) | (b - a - c) | (c - a - b)) & achievements
    print(f"Rare achievements (1 player): {rare_achiev}")


def main():
    players: set = [
        {"alice", "first_kill", "level_10", "treasure_hunter", "speed_demon"},
        {"bob", "first_kill", "level_10", "boss_slayer", "collector"},
        {"charlie", "level_10", "treasure_hunter", "boss_slayer", "speed_demon",
         "perfectionist"}]
    ft_achievement_tracker(players)


main()
