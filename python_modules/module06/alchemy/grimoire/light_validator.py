def validate_ingredients(ingredients: str) -> str:
    from .light_spellbook import light_spell_allowed_ingredients
    allowed_ingredients = light_spell_allowed_ingredients()
    for ingredient in allowed_ingredients:
        if ingredient in ingredients:
            return (ingredients + " - VALID")
        else:
            return (ingredients + " - INVALID")
