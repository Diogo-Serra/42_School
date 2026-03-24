#!/usr/bin/env python3
import sys


def ft_command_quest() -> None:
    print("=== Command Quest ===\n")
    if (len(sys.argv) == 1):
        print(f"Program name: {sys.argv[0][2:]}")
        print("No arguments provided!")
        print(f"Total arguments: {len(sys.argv)}")
    elif (len(sys.argv) > 1):
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
