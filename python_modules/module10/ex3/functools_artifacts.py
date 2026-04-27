from functools import reduce


"""
def spell_reducer(spells: list[int], operation: str) -> int
def partial_enchanter(base_enchantment: Callable) -> dict[str, Callable]
def memoized_fibonacci(n: int) -> int
def spell_dispatcher() -> Callable[[Any], str]
"""


spells = [1, 5, 7, 2, 3]


def spell_reducer(spells: list[int], operation: str) -> int:
    if operation == "add":
        return reduce(lambda x, y: x + y, spells)
    if operation == "mul":
        return reduce(lambda x, y: x * y, spells)
    if operation == "max":
        return reduce(lambda x, y: x if x > y else y, spells)
    if operation == "min":
        return reduce(lambda x, y: x if x < y else y, spells)


if __name__ == "__main__":
    result = spell_reducer(spells, "add")
    print(result)
    result = spell_reducer(spells, "mul")
    print(result)
    result = spell_reducer(spells, "max")
    print(result)
    result = spell_reducer(spells, "min")
    print(result)
