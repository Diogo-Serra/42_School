#!/usr/bin/env python3

def ft_garden_intro() -> None:
    name: str = "Rose"
    height: int = 25
    age: int = 30
    print("=== Welcome to My Garden ===")
    print(f"Name: {name.capitalize()}\nHeight: {height}cm\nAge: {age} days\n")
    print("=== End of Program ===")


# runs the code only when the file is executed directly
if __name__ == "__main__":
    ft_garden_intro()
