from functools import reduce, partial
from collections.abc import Callable


"""
def spell_reducer(spells: list[int], operation: str) -> int
def partial_enchanter(base_enchantment: Callable) -> dict[str, Callable]
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
