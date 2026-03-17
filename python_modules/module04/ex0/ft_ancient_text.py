#!/usr/bin/env python3


def ft_ancient_text():
    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===\n")
    try:
        f = open("ancient_fragment.txt", "rt")
        print(f"Accessing Storage Vault: {f.name}")
        print("Connection established...\n")
    except (FileNotFoundError, FileExistsError):
        print("ERROR: Storage vault not found.")
    print("RECOVERED DATA:")
    print(f.read())
    f.close()
    print("\nData recovery complete. Storage unit disconnected.")


ft_ancient_text()
