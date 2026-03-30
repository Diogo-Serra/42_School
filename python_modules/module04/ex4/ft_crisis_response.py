#!/usr/bin/env python3
from sys import stderr, stdout


def handle_file_access(filename: str) -> None:
    try:
        with open(filename, "r") as vault:
            content: str = vault.read()
            stdout.write(f"SUCCESS: Archive recovered - \"{content}\"")
    except FileNotFoundError:
        stderr.write("RESPONSE: Archive not found in storage matrix")
    except PermissionError:
        stderr.write("RESPONSE: Security protocols deny access")
    except Exception:
        stderr.write("RESPONSE: Unexpected system anomaly")


def ft_crisis_response() -> None:
    print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===")

    stderr.write("CRISIS ALERT: Attempting access to 'lost_archive.txt'...")
    handle_file_access("lost_archive.txt")
    stdout.write("STATUS: Crisis handled, system stable\n")

    stderr.write("CRISIS ALERT: Attempting access to 'classified_vault.txt'...")
    handle_file_access("classified_vault.txt")
    stdout.write("STATUS: Crisis handled, security maintained\n")

    stdout.write("ROUTINE ACCESS: Attempting access to 'standard_archive.txt'...")
    try:
        with open("standard_archive.txt", "w") as vault:
            vault.write("Knowledge preserved for humanity")
    except Exception:
        pass
    handle_file_access("standard_archive.txt")
    sys.stdout.write("STATUS: Normal operations resumed\n")

    sys.stdout.write("All crisis scenarios handled successfully. Archives secure.")


ft_crisis_response()
