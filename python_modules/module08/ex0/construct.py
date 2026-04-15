#!/usr/bin/env python3
from sys import executable, base_prefix, prefix
from os import path, getenv
from site import getsitepackages


path_var = executable
env_var = getenv("VIRTUAL_ENV")
env_name = path.basename(env_var)

if not env_var:

    print("\nMATRIX STATUS: You're still plugged in\n")

    print(f"Current Python: {path_var}")
    print("Virtual Environment: None detected")

    print("\nWARNING: You're in the global environment!")
    print("The machines can see everything you install.")

    print("\nTo enter the construct, run:")
    print("python -m venv matrix_env")
    print("source matrix_env/bin/activate # On Unix")
    print("matrix_env\\Scripts\\activate # On Windows")

    print("\nThen run this program again.")
else:
    print("\nMATRIX STATUS: Welcome to the construct\n")
    print(f"Current Python: {path_var}")
    print(f"Virtual Environment: {env_name}")
    print(f"Environment Path: {env_var}")
    print("\nSUCCESS: You're in an isolated environment!\n")
    print("Safe to install packages without affecting")
    print("the global system.")

    package = getsitepackages()[0]
    print(f"\nPackage installation path:\n{(package)}")
