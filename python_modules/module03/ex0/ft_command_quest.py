#!/usr/bin/env python3
import sys

"""
=== Command Quest ===
No arguments provided!
Program name: ft_command_quest.py
Total arguments: 1

$> python3 ft_command_quest.py hello world 42
=== Command Quest ===
Program name:
Arguments received: 3
Argument 1: hello
Argument 2: world
Argument 3: 42
Total arguments: 4

$> python3 ft_command_quest.py "Data Quest"
=== Command Quest ===
Program name: ft_command_quest.py
Arguments received: 1
Argument 1: Data Quest
Total arguments: 2
"""


def ft_command_quest() -> None:
    print("=== Command Quest ===\n")
    if (len(sys.argv) > 1):
        print(f"Program name: {sys.argv[0][2:]}")
        print(f"Arguments received: {len(sys.argv) - 1}")
        for i, arg in enumerate(sys.argv[1:], start=1):
            print(f"Argument {i}: {arg}")
        print(f"Total arguments: {len(sys.argv)}")
    else:
        print("No arguments provided!")
        print(f"Program name: {sys.argv[0][2:]}")
        print(f"Total arguments: {len(sys.argv)}")


ft_command_quest()
