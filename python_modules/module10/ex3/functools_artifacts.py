from functools import reduce, partial, lru_cache, singledispatch
from collections.abc import Callable
from typing import Any


"""
def memoized_fibonacci(n: int) -> int
def spell_dispatcher() -> Callable[[Any], str]
"""


spells = [1, 5, 7, 2, 3]


def base_enchantment(
    power: int,
    element: str,
    target: str
) -> str:
    return f"Power: {power}, Element: {element}, Target: {target}"


def spell_reducer(spells: list[int], operation: str) -> int:
    if not spells:
        return 0
    try:
        if operation == "add":
            return reduce(lambda x, y: x + y, spells)
        elif operation == "mul":
            return reduce(lambda x, y: x * y, spells)
        elif operation == "max":
            return reduce(lambda x, y: x if x > y else y, spells)
        elif operation == "min":
            return reduce(lambda x, y: x if x < y else y, spells)
        else:
            return "Operation not recognized"
    except Exception as e:
        print(e)


def partial_enchanter(base_enchantment: Callable) -> dict[str, Callable]:
    return {
        "fire": partial(base_enchantment, 50, "fire", "itself"),
        "ice": partial(base_enchantment, 50, "ice", "itself"),
        "lightning": partial(base_enchantment, 50, "lightning", "itself"),
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
        return f"Damage spell deals {spell} damage"

    @cast.register
    def _(spell: str) -> str:
        return f"Enchantment cast: {spell}"

    @cast.register
    def _(spell: list) -> str:
        return f"Multi-cast with {len(spell)} spells"

    return cast


if __name__ == "__main__":
    result = spell_reducer(spells, "add")
    print(result)
    result = spell_reducer(spells, "mul")
    print(result)
    result = spell_reducer(spells, "max")
    print(result)
    result = spell_reducer(spells, "min")
    print(result)
    result = spell_reducer(spells, "test")
    print(result)

    result = partial_enchanter(base_enchantment)
    print(result['ice']())

    print(memoized_fibonacci(10))

    cast_spell = spell_dispatcher()
    print(cast_spell(42))
    print(cast_spell("shield"))
    print(cast_spell(["fire", "ice", "wind"]))
    print(cast_spell(3.14))
