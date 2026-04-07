from .dark_spellbook import dark_spell_allowed_ingredients


def validate_ingredients(ingredients: str) -> str:
    allowed_ingredients = str(dark_spell_allowed_ingredients())
    if allowed_ingredients in ingredients:
        return (allowed_ingredients + " - VALID")
    else:
        return (allowed_ingredients + " - INVALID")
