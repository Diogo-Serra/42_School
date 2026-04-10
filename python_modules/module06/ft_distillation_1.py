import alchemy


print("=== Distillation 1 ===")
print("Using: 'import alchemy' structure to access potions")
print(f"Testing strength_potion: "
      f"{alchemy.potions.strength_potion()}")
print(f"Testing heal alias: {alchemy.heal()}")
