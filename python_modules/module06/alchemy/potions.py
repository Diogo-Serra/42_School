import alchemy as basic_elements


def healing_potion():
    return (f"Healing potion brewed with {basic_elements.create_fire()} "
            f"and {basic_elements.create_water()}")


def strength_potion():
    return (f"Strength potion brewed with "
            f"{basic_elements.elements.create_earth()} "
            f"and {basic_elements.create_fire()}")


def invisibility_potion():
    return (f"Invisibility potion brewed with "
            f"{basic_elements.elements.create_air()} and "
            f"{basic_elements.elements.create_water()}")


def wisdom_potion():
    return (f"Wisdom potion brewed with all elements: "
            f"{basic_elements.create_fire()} and "
            f"{basic_elements.create_water()} and "
            f"{basic_elements.elements.create_earth()} and "
            f"{basic_elements.elements.create_air()} and ")
