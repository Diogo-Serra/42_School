def ft_water_reminder() -> None:
    days = int(input("Days since last watering: "))
    if days <= 2:
        print("Plants are fine.")
    else:
        print("Water the plants!")
