#!/usr/bin/env python3
import ex0.CreatureFactory as cf


def factory_tester(factory_object):
    print("Testing factory")
    try:
        if type(factory_object) is cf.FlameFactory:
            factory = cf.FlameFactory()
            flame1 = factory.create_base()
            print(flame1.describe())
            print(flame1.attack())
            flame2 = factory.create_evolved()
            print(flame2.describe())
            print(flame2.attack())
        else:
            factory = cf.AquaFactory()
            aqua1 = factory.create_base()
            print(aqua1.describe())
            print(aqua1.attack())
            aqua2 = factory.create_evolved()
            print(aqua2.describe())
            print(aqua2.attack())
    except Exception as error:
        print(error)


def attack_tester(factory1, factory2):

    print("\nTesting battle")

    factory = cf.FlameFactory()
    flame1 = factory.create_base()
    factory = cf.AquaFactory()
    aqua1 = factory.create_base()
    print(flame1.describe())
    print(" vs.")
    print(aqua1.describe())
    print(" fight!")

    print(flame1.attack())
    print(aqua1.attack())


factory_tester(cf.FlameFactory())
print()
factory_tester(cf.AquaFactory())
attack_tester(cf.FlameFactory, cf.AquaFactory)
