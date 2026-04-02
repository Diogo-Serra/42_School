#!/usr/bin/env/python3

def record_spell(spell_name: str, ingredients: str) -> str:
    from validator import validate_ingredients

    spell_name = validate_ingredients(ingredients)
    if "VALID" in spell_name:
        print(f"Spell recorded: {spell_name} ([validation_result])")
    else:
        print("")
