import ex0.CreatureFactory as cf

print("Testing factory")
fire_factory = cf.FlameFactory()

flame1 = fire_factory.create_base()
print(flame1.describe())
print(flame1.attack())

flame2 = fire_factory.create_evolved()
print(flame2.describe())
print(flame2.attack())

print("\nTesting factory")
water_factory = cf.AquaFactory()

aqua1 = water_factory.create_base()
print(aqua1.describe())
print(aqua1.attack())

aqua2 = water_factory.create_evolved()
print(aqua2.describe())
print(aqua2.attack())

print("\nTesting battle")

print(flame1.describe())
print("vs")
print(aqua1.describe())
print("fight!")

print(flame1.attack())
print(aqua1.attack())
