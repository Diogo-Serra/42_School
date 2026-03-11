#!/usr/bin/env python3

# No classes in this exercise. No OOP
def ft_garden_intro() -> None:
    name: str = (str)("Rose")
    height: int = (int)(25)
    age: int = (int)(30)
    print("=== Welcome to My Garden ===")
    print(f"Name: {name.capitalize()}\nHeight: {height}cm\nAge: {age} days\n")
    print("=== End of Program ===")


# runs the code only when the file is executed directly and not
# when it's imported as a module by another file.
if __name__ == "__main__":
    ft_garden_intro()
