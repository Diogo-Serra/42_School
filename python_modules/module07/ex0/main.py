#!/usr/bin/env python3
from CreatureCard import CreatureCard


def tester():
    print("=== DataDeck Card Foundation ===\n")

    print("Testing Abstract Base Class Design:\n")
    token = CreatureCard("Fire Dragon", 5, "Legendary", 7, 5)

    print("CreatureCard Info:")
    token.get_card_info()


tester()
