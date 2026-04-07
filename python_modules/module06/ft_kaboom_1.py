from alchemy.grimoire.dark_spellbook import dark_spell_record


print("=== Kaboom 1 ===")
print("Access to alchemy/grimoire/dark_spellbook.py directly")
print("Test import now - THIS WILL RAISE AN UNCAUGHT EXCEPTION")
spell = dark_spell_record("Fantasy", "earth, wind, fire")
print(f"Testing record dark spell: {spell}")
