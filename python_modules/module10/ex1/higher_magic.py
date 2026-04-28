from collections.abc import Callable


def fireball(target: str, power: int) -> str:
    return f"{target} attacks with fireball with {power} attack power"


def heal(target: str, power: int) -> str:
    return f"{target} heals itself {power}HP"


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    return lambda target, power: (spell1(target, power), spell2(target, power))


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    return lambda target, power: base_spell(target, power * multiplier)


def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    return lambda target, power: spell(
        target, power) if condition(target, power) else "Spell fizzled"


def spell_sequence(spells: list[Callable]) -> Callable:
    return lambda target, power: [spell(target, power) for spell in spells]


if __name__ == "__main__":
    try:
        spell_list: list[Callable] = [fireball, heal]

        print("Testing spell combiner...")
        combined = spell_combiner(fireball, heal)
        result = combined("Dragon", 50)
        print(f"Combined spell result: {result[0]}, {result[1]}")

        print("Testing power amplifier...")
        amplified = power_amplifier(fireball, 3)
        print(f"Original: {fireball('Dragon', 10)}")
        print(f"Amplified: {amplified('Dragon', 10)}")

        print("Testing conditional caster...")
        cond = conditional_caster(lambda t, p: p > 50, fireball)
        print(cond("Dragon", 60))
        print(cond("Dragon", 30))

        print("Testing spell sequence...")
        seq = spell_sequence(spell_list)
        print(seq("Dragon", 50))
    except Exception as e:
        print(e)
