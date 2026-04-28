from collections.abc import Callable
from functools import wraps
from time import sleep


class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        cleaned = name.strip()
        return len(cleaned) >= 3 and all(
            c.isalpha() or c.isspace() for c in name
        )

    def cast_spell(self, spell_name: str, power: int) -> str:
        return f"Successfully cast {spell_name} with {power} power"


def spell_timer(func: Callable) -> Callable:
    from time import perf_counter

    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Casting {func.__name__}...")
        start = perf_counter()
        result = func(*args, **kwargs)
        elapsed = perf_counter() - start
        print(f"Spell completed in {elapsed:.3f} seconds")
        return result
    return wrapper


def power_validator(min_power: int) -> Callable:
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs):
            if "power" in kwargs:
                power = kwargs["power"]
            elif args and isinstance(args[0], (int, float)):
                power = args[0]
            elif len(args) > 1 and isinstance(args[1], (int, float)):
                power = args[1]
            else:
                return "Insufficient power for this spell"

            if power < min_power:
                return "Insufficient power for this spell"
            return func(*args, **kwargs)
        return wrapper
    return decorator


MageGuild.cast_spell = power_validator(10)(MageGuild.cast_spell)


def retry_spell(max_attempts: int) -> Callable:
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs):
            attempt = 1
            while attempt <= max_attempts:
                try:
                    return func(*args, **kwargs)
                except Exception:
                    if attempt < max_attempts:
                        print(
                            "Spell failed, retrying... "
                            f"(attempt {attempt}/{max_attempts})"
                        )
                    attempt += 1
            return f"Spell casting failed after {max_attempts} attempts"
        return wrapper
    return decorator


if __name__ == "__main__":
    @spell_timer
    def fireball() -> str:
        sleep(0.101)
        return "Fireball cast!"

    @retry_spell(3)
    def broken_spell() -> str:
        raise RuntimeError("boom")

    @retry_spell(3)
    def waaagh_spell() -> str:
        return "Waaaaaaagh spelled !"

    print("Testing spell timer...")
    result = fireball()
    print(f"Result: {result}")

    print("Testing retrying spell...")
    print(broken_spell())
    print(waaagh_spell())

    print("Testing MageGuild...")
    guild = MageGuild()
    print(MageGuild.validate_mage_name("Gandalf"))
    print(MageGuild.validate_mage_name("x1"))
    print(guild.cast_spell("Lightning", 15))
    print(guild.cast_spell("Lightning", 5))
