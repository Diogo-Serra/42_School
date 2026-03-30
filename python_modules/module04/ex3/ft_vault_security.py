#!/usr/bin/env python3

def ft_vault_security() -> None:
    print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===\n")
    print("Initiating secure vault access...")
    print("Vault connection established with failsafe protocols")

    print("\nSECURE EXTRACTION:")
    try:
        with open("classified_data.txt", "r") as vault:
            keys: str = vault.read()
            print(keys)
    except (FileExistsError, FileNotFoundError) as e:
        print(f"Error: {e}")
    print("\nSECURE PRESERVATION:")
    try:
        with open("security_protocols.txt", "r") as vault:
            sec_protocol = vault.read()
            print(sec_protocol)
    except (FileExistsError, FileNotFoundError) as e:
        print(f"Error: {e}")
    finally:
        print("Vault automatically sealed upon completion")
        print("\nAll vault operations completed with maximum security.")


ft_vault_security()
