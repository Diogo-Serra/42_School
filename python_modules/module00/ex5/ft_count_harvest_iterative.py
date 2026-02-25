def ft_count_harvest_iterative() -> None:
    days = int(input("Days until harvest: "))
    count = 1
    while count <= days:
        print(count)
        count += 1
    print("Ready to harvest!")
