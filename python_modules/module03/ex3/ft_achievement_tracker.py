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


def ft_achievement_tracker(players: set):
    print("=== Achievement Tracker System ===")
    for i in set:
        print(i)


def main():
    players: set = {"alice", "bob", "charlie"}
    ft_achievement_tracker()
