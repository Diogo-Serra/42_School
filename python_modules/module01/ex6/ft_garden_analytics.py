#!/usr/bin/env python3

# Plant family tree: Plant -> FloweringPlant -> PrizeFlower
class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age
        self.initial_height = height

    def grow(self) -> None:
        self.height += 1

    def __str__(self) -> str:
        return f"{self.name}: {self.height}cm"


class FloweringPlant(Plant):
    def __init__(self, name: str, height: int, age: int, color: str) -> None:
        super().__init__(name, height, age)
        self.color = color

    def bloom(self) -> str:
        return "blooming"

    def __str__(self) -> str:
        return (f"{self.name}: {self.height}cm, "
                f"{self.color} flowers ({self.bloom()})")


# PrizeFlower inherits the full chain : Plant -> FloweringPlant -> PrizeFlower
class PrizeFlower(FloweringPlant):
    def __init__(self, name: str, height: int, age: int,
                 color: str, prize_points: int) -> None:
        super().__init__(name, height, age, color)
        self.prize_points = prize_points

    def __str__(self) -> str:
        return f"{super().__str__()}, Prize points: {self.prize_points}"


class GardenManager:
    # Class variable : shared across all instances.
    total_gardens: int = 0

    def __init__(self, owner: str) -> None:
        self.owner = owner
        self.plants: list = []
        GardenManager.total_gardens += 1

    # Instance method : operates on this specific garden's data.
    def add_plant(self, plant: Plant) -> None:
        self.plants.append(plant)
        print(f"Added {plant.name} to {self.owner}'s garden")

    def grow_all(self) -> None:
        print(f"\n{self.owner} is helping all plants grow...")
        for plant in self.plants:
            plant.grow()
            print(f"{plant.name} grew 1cm")

    def report(self) -> None:
        print(f"\n=== {self.owner}'s Garden Report ===")
        print("Plants in garden:")
        for plant in self.plants:
            print(f"- {plant}")
        stats = GardenManager.GardenStats
        growth = stats.total_growth(self.plants)
        types = stats.count_types(self.plants)
        print(f"\nPlants added: {len(self.plants)}, Total growth: {growth}cm")
        print(f"Plant types: {types['regular']} regular, "
              f"{types['flowering']} flowering, {types['prize']} "
              f"prize flowers")

    # @classmethod : works on the class itself, can create instances.
    @classmethod
    def create_garden_network(cls, owners: list) -> list:
        return [cls(owner) for owner in owners]

    # @staticmethod : utility function, needs no instance or class data.
    @staticmethod
    def validate_height(height: int) -> bool:
        return height > 0

    # Nested class : groups statistics logic
    class GardenStats:
        @staticmethod
        def total_growth(plants: list) -> int:
            return sum(p.height - p.initial_height for p in plants)

        @staticmethod
        def count_types(plants: list) -> dict:
            return {
                "regular": sum(1 for p in plants if type(p) is Plant),
                "flowering": sum(1 for p in plants if type(p) is
                                 FloweringPlant),
                "prize": sum(1 for p in plants if type(p) is PrizeFlower)
            }

        @staticmethod
        def garden_score(plants: list) -> int:
            score = 0
            for p in plants:
                score += p.height + p.age
                if isinstance(p, PrizeFlower):
                    score += p.prize_points
            return score

    def score(self) -> int:
        return GardenManager.GardenStats.garden_score(self.plants)


def ft_garden_analytics() -> None:
    print("=== Garden Management System Demo ===")
    alice, bob = GardenManager.create_garden_network(["Alice", "Bob"])

    alice.add_plant(Plant("Oak Tree", 100, 18))
    alice.add_plant(FloweringPlant("Rose", 25, 5, "red"))
    alice.add_plant(PrizeFlower("Sunflower", 50, 7, "yellow", 10))

    bob.add_plant(Plant("Cactus", 15, 40))
    bob.add_plant(FloweringPlant("Tulip", 30, 7, "purple"))

    alice.grow_all()
    alice.report()

    print(f"\nHeight validation test: {GardenManager.validate_height(10)}")
    print(f"Garden scores - Alice: {alice.score()}, Bob: {bob.score()}")
    print(f"Total gardens managed: {GardenManager.total_gardens}")


if __name__ == "__main__":
    ft_garden_analytics()
