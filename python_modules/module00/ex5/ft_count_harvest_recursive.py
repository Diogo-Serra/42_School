def ft_count_harvest_recursive():
    def helper(count, days):
        if count > days:
            print("Ready to harvest!")
        else:
            print(count)
            helper(count + 1, days)
    days = int(input("Days until harvest: "))
    helper(1, days)
