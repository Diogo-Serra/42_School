from typing import Any, Callable


def mage_counter() -> Callable:
    inter_counter: int = 0

    def count():
        nonlocal inter_counter
        inter_counter += 1
        return inter_counter

    return count


def spell_accumulator(initial_power: int) -> Callable:
    accumulated: int = 0

    def accumulator(initial_power):
        nonlocal accumulated
        accumulated += initial_power
        return accumulated
    return accumulator


def enchantment_factory(enchantment_type: str) -> Callable:
    enchantment: str = enchantment_type + " "

    def enchant(item: str) -> str:
        nonlocal enchantment
        enchanted_item = enchantment + item
        return enchanted_item

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


print("=== Mage Counter ===")
counting = mage_counter()
print(counting())
print(counting())

print("=== Mage Accumulator ===")
accumulator = spell_accumulator(5)
print(accumulator(5))
print(accumulator(50))
print(accumulator(45))

print("=== Enchantment Factory ===")
enchantment = enchantment_factory("Flaming")
print(enchantment('Sword'))
enchantment = enchantment_factory("Ice")
print(enchantment('Staff'))

print("=== Memory Vault ===")
vault = memory_vault()
vault["store"]("secret", 42)
print(vault["recall"]("secret"))
print(vault["recall"]("missing"))
