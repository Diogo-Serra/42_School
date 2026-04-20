from typing import Callable

# def spell(target: str, power: int) -> str
# def spell_combiner(spell1: Callable, spell2: Callable) -> Callable
# def power_amplifier(base_spell: Callable, multiplier: int) -> Callable
# def conditional_caster(condition: Callable, spell: Callable) -> Callable
# def spell_sequence(spells: list[Callable]) -> Callable

def fireball(target: str, power: int) -> str:
    return f"{target} attacks with fireball with {power} power"


def heal(target: str, power: int) -> str:
    return f"{target} heals itself with {power} power"


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    return lambda target, power: spell1(target, power) + spell2(target, power)


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    return lambda target, power: base_spell(target, power * multiplier)

def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    return lambda target, power: spell(
            target, power) if condition is True else False


condition = lambda target, power: True if power > 50 else False


combined = spell_combiner(fireball, heal)
print(combined("Wizard", 50))

amplified = power_amplifier(fireball, 5)
print(amplified("Wizard", 5))

conditional = conditional_caster(condition, fireball)
print(condition("Wizard", 30))


