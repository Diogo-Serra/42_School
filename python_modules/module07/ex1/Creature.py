from ex0.Creature import Creature
from .Capabilities import HealCapability as Heal
from .Capabilities import TransformCapability as Transform


class Sproutling(Creature, Heal):

    def __init__(self) -> None:
        super().__init__("Sproutling", "Grass")
        self.basic = "Vine Whip"

    def attack(self) -> str:
        return f"{self.name} uses {self.basic}!"

    def heal(self, target: Creature = None) -> str:
        if target is None:
            target = self
        if target is self:
            return f"{self.name} heals itself for a small amount"
        else:
            return f"{self.name} heals {target.name} for a small amount"


class Bloomelle(Creature, Heal):

    def __init__(self) -> None:
        super().__init__("Bloomelle", "Grass/Fairy")
        self.basic = "Petal Dance"

    def attack(self) -> str:
        return f"{self.name} uses {self.basic}!"

    def heal(self, target: Creature = None) -> str:
        if target is None:
            target = self
        if target is self:
            return f"{self.name} heals itself for a large amount"
        else:
            return f"{self.name} heals {target.name} for a large amount"


class Shiftling(Creature, Transform):

    def __init__(self) -> None:
        super().__init__("Shiftling", "Normal")

    def attack(self) -> str:
        if self.status == "base":
            return f"{self.name} attacks normally."
        else:
            return f"{self.name} performs a boosted strike!"

    def transform(self) -> str:
        self.status = "evolved"
        return f"{self.name} shifts into a sharper form!"

    def revert(self) -> str:
        self.status = "base"
        return f"{self.name} returns to normal."


class Morphagon(Creature, Transform):

    def __init__(self) -> None:
        super().__init__("Morphagon", "Normal/Dragon")

    def attack(self) -> str:
        if self.status == "base":
            return f"{self.name} attacks normally."
        else:
            return f"{self.name} unleashes a devastating morph strike!"

    def transform(self) -> str:
        self.status = "evolved"
        return f"{self.name} morphs into a dragonic battle form!"

    def revert(self) -> str:
        self.status = "base"
        return f"{self.name} stabilizes its form."
