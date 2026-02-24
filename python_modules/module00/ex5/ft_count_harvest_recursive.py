def ft_count_harvest_recursive(count):
    if count > 5:
        print("Ready to harvest!")
    else:
        print(count)
        ft_count_harvest_recursive(count + 1)

