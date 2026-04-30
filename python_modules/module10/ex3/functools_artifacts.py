from functools import reduce, partial, lru_cache, singledispatch
from collections.abc import Callable
from typing import Any
import operator


def base_enchantment(
    power: int,
    element: str,
    target: str
) -> str:
    return f"Power: {power}, Element: {element}, Target: {target}"


def spell_reducer(spells: list[int], operation: str) -> int | str:
    if not spells:
        return 0
    try:
        if operation == "add":
            return reduce(operator.add, spells)
        elif operation == "multiply":
            return reduce(operator.mul, spells)
        elif operation == "max":
            return reduce(lambda x, y: x if x > y else y, spells)
        elif operation == "min":
            return reduce(lambda x, y: x if x < y else y, spells)
        else:
            raise ValueError("Operation not recognized")
    except Exception:
        raise ValueError(f"Error on reduce operation: {operation}")


def partial_enchanter(base_enchantment: Callable) -> dict[str, Callable]:
    return {
        "fire": partial(base_enchantment, 50, "fire"),
        "ice": partial(base_enchantment, 50, "ice"),
        "lightning": partial(base_enchantment, 50, "lightning"),
    }


@lru_cache
def memoized_fibonacci(n: int) -> int:
    if n <= 1:
        return n
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


def spell_dispatcher() -> Callable[[Any], str]:

    @singledispatch
    def cast(spell: Any) -> str:
        return "Unknown spell type"

    @cast.register
    def _(spell: int) -> str:
        return f"Damage spell: {spell} damage"

    @cast.register
    def _(spell: str) -> str:
        return f"Enchantment: {spell}"

    @cast.register
    def _(spell: list) -> str:
        return f"Multi-cast: {len(spell)} spells"

    return cast


if __name__ == "__main__":

    spell_powers = [27, 43, 40, 37, 37, 49]

    try:

        print()
        print("Testing spell reducer...")
        print(f"Sum: {spell_reducer(spell_powers, 'add')}")
        print(f"Max: {spell_reducer(spell_powers, 'max')}")
        print(f"Min: {spell_reducer(spell_powers, 'min')}")
        print(f"Product: {spell_reducer(spell_powers, 'multiply')}")

        print()
        print("Testing partial enchanter...")
        enchantments = partial_enchanter(base_enchantment)
        print(enchantments['ice']("Dragon"))

        print()
        print("Testing memoized fibonacci...")
        print(f"Fib(15): {memoized_fibonacci(15)}")
        print(f"Fib(20): {memoized_fibonacci(20)}")
        print(f"Fib(16): {memoized_fibonacci(16)}")

        print()
        print("Testing spell dispatcher...")
        cast_spell = spell_dispatcher()
        print(cast_spell(42))
        print(cast_spell("fireball"))
        print(cast_spell(["fire", "ice", "wind"]))
        print(cast_spell(3.14))
        print()

    except Exception as error:
        print(error)
