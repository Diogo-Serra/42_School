#!/usr/bin/env python3

def ft_count_harvest_iterative() -> None:
    days: int = int(input("Days until harvest: "))
    count: int = 1
    while count <= days:
        print(count)
        count += 1
    print("Ready to harvest!")


ft_count_harvest_iterative()
