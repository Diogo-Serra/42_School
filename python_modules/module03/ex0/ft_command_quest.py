#!/usr/bin/env python3
from sys import argv


def ft_command_quest() -> None:
    print("=== Command Quest ===\n")
    if (len(argv) == 1):
        print(f"Program name: {argv[0][2:]}")
        print("No arguments provided!")
        print(f"Total arguments: {len(argv)}")
    elif (len(argv) > 1):
        print(f"Program name: {argv[0][2:]}")
        print(f"Arguments received: {len(argv) - 1}")
        for i, arg in enumerate(argv[1:], start=1):
            print(f"Argument {i}: {arg}")
        print(f"Total arguments: {len(argv)}")
    else:
        print("No arguments provided!")
        print(f"Program name: {argv[0][2:]}")
        print(f"Total arguments: {len(argv)}")


ft_command_quest()
