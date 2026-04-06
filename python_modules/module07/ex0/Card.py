from abc import ABC, abstractmethod


class Card(ABC):
    def __init__(self, name: str, cost: int, rarity: str) -> None:
        self.name = name
        self.cost = cost
        self.rarity = rarity

    @abstractmethod
    def play(self, game_state: dict):
        ...

    def get_card_info(self) -> str:
        return (f"'name': {self.name}, 'cost': {self.cost}, "
               f"'rarity': {self.rarity}, 'type': pass, "
               f"'attack': pass, 'health': pass")

    def is_playable(self, available_mana: int) -> bool:
        if available_mana <= self.cost:
            return False
        return True
