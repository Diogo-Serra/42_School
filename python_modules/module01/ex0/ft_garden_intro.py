#!/usr/bin/env python3

def ft_garden_intro() -> None:
    name: str = (str)("Rose")
    height: int = (int)(25)
    age: int = (int)(30)
    print("=== Welcome to My Garden ===")
    print(f"Name: {name.capitalize()}\nHeight: {height}cm\nAge: {age} days\n")
    print("=== End of Program ===")


if __name__ == "__main__":
    ft_garden_intro()
