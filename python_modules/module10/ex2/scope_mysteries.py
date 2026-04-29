from collections.abc import Callable
from typing import Any


def mage_counter() -> Callable:

    inter_counter: int = 0

    def count():
        nonlocal inter_counter
        inter_counter += 1
        return inter_counter

    return count


def spell_accumulator(initial_power: int) -> Callable:

    accumulated: int = initial_power

    def accumulator(amount: int) -> int:
        nonlocal accumulated
        accumulated += amount
        return accumulated

    return accumulator


def enchantment_factory(enchantment_type: str) -> Callable:

    def enchant(item: str) -> str:
        return f"{enchantment_type} {item}"

    return enchant


def memory_vault() -> dict[str, Callable]:

    memory: dict[str, Any] = {}

    def store(key: str, value: Any) -> None:
        memory[key] = value

    def recall(key: str) -> Any | str:
        if key in memory:
            return memory[key]
        return "Memory not found"

    return {"store": store, "recall": recall}


if __name__ == "__main__":

    try:

        print("Testing mage counter...")
        counter_a = mage_counter()
        counter_b = mage_counter()
        print(f"counter_a call 1: {counter_a()}")
        print(f"counter_a call 2: {counter_a()}")
        print(f"counter_b call 1: {counter_b()}")

        print()

        print("Testing spell accumulator...")
        accumulator = spell_accumulator(50)
        print(f"Base 50, add 50: {accumulator(50)}")
        print(f"Base 50, add 25: {accumulator(25)}")

        print()

        print("Testing enchantment factory...")
        flaming = enchantment_factory("Flaming")
        print(flaming("Staff"))
        ice = enchantment_factory("Earthen")
        print(ice("Shield"))

        print()

        print("Testing memory vault...")
        vault = memory_vault()
        print("Store 'secret' = 42")
        vault["store"]("secret", 42)
        print(f"Recall 'secret': {vault['recall']('secret')}")
        print(f"Recall 'unknown': {vault['recall']('unknown')}")

    except Exception as e:
        print(e)
