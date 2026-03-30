#!/usr/bin/env python3
from typing import IO


def ft_ancient_text() -> None:
    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===\n")
    try:
        f: IO[str] = open("ancient_fragment.txt", "r")
        print(f"Accessing Storage Vault: {f.name}")
        print("Connection established...\n")
        print("RECOVERED DATA:")
        print(f.read())
        # f.close()
    except (FileNotFoundError, FileExistsError):
        print("ERROR: Storage vault not found.")
    print("\nData recovery complete. Storage unit disconnected.")


ft_ancient_text()
