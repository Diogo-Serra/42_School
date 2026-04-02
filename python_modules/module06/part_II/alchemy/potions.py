#!/usr/bin/env python3
import part_I.alchemy as alchemy_I


def healing_potion():
    return (f"Healing potion brewed with [{alchemy_I.create_fire}] "
            f"and [{alchemy_I.create_water}]")


def strength_potion():
    return (f"Healing potion brewed with [{alchemy_I.create_fire}] "
            f"and [{alchemy_I.create_water}]")


def invisibility_potion():
    return (f"Invisibility potion brewed with "
            f"[{alchemy_I.elements.create_air()}] and "
            f"[{alchemy_I.elements.create_water()}]")


def wisdom_potion():
    return (f"Wisdom potion brewed with all elements: [all_four_results]")
