def validate_ingredients(ingredients: str) -> str:
    valid = ["fire", "water", "earth", "air"]
    ingredients_parsed = ingredients.split()
    for ingredient in ingredients_parsed:
        if ingredient not in valid:
            return f"{ingredients} - INVALID"
    return f"{' '.join(ingredients_parsed)} - VALID"
