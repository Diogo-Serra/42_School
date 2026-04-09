#!/usr/bin/env python3
import os
import sys

path = sys.executable
env = os.getenv("VIRTUAL_ENV")
if not env:

    print("\nMATRIX STATUS: You're still plugged in\n")

    print(f"Current Python: {path}")
    print("Virtual Environment: None detected")

    print("\nWARNING: You're in the global environment!")
    print("The machines can see everything you install.")

    print("\nTo enter the construct, run:")
    print("python -m venv matrix_env")
    print("source matrix_env/bin/activate # On Unix")
    print("matrix_env\\Scripts\\activate # On Windows")

    print("\nThen run this program again.")
else:
    print(f"Virtual environment detected\nPath: [{env}]")
