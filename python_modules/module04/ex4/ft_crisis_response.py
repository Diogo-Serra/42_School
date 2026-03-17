#!/usr/bin/env python3


def handle_file_access(filename):
    try:
        with open(filename, "r") as vault:
            content = vault.read()
            print(f"SUCCESS: Archive recovered - \"{content}\"")
    except FileNotFoundError:
        print("RESPONSE: Archive not found in storage matrix")
    except PermissionError:
        print("RESPONSE: Security protocols deny access")
    except Exception:
        print("RESPONSE: Unexpected system anomaly")


def ft_crisis_response():
    print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===")

    print("CRISIS ALERT: Attempting access to 'lost_archive.txt'...")
    handle_file_access("lost_archive.txt")
    print("STATUS: Crisis handled, system stable\n")

    print("CRISIS ALERT: Attempting access to 'classified_vault.txt'...")
    handle_file_access("classified_vault.txt")
    print("STATUS: Crisis handled, security maintained\n")

    print("ROUTINE ACCESS: Attempting access to 'standard_archive.txt'...")
    try:
        with open("standard_archive.txt", "w") as vault:
            vault.write("Knowledge preserved for humanity")
    except Exception:
        pass
    handle_file_access("standard_archive.txt")
    print("STATUS: Normal operations resumed\n")

    print("All crisis scenarios handled successfully. Archives secure.")


ft_crisis_response()
