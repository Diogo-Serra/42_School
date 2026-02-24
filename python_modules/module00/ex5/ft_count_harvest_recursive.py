def ft_count_harvest_recursive(count, days):
    if days == 0:
        days = int(input("Days until harvest: "))
    if count > days:
        print("Ready to harvest!")
    else:
        print(count)
        ft_count_harvest_recursive(count + 1, days)
