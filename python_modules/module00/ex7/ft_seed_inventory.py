def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
    if unit == "packets":
        print(seed_type, "seeds:", quantity, unit, "available")
    if unit == "grams":
        print(seed_type, "seeds:", quantity, unit, "total")
    if unit == "area":
        print(seed_type, "seeds:", quantity, unit, "square meters")
