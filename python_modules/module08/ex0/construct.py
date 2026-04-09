#!/usr/bin/env python3
from os import getenv

var = getenv("VIRTUAL_ENV")
if not var:
    print("No virtual environment: python3 -m venv matrix_env")
else:
    print(f"Should detect virtual environment and show details: [{var}]")
