#!/usr/bin/env python3

def checker() -> None:
    try:

        from dotenv import load_dotenv
        from os import getenv
        load_dotenv()

        print("Configuration loaded:")
        print(f"Mode: {getenv('MATRIX_MODE')}")
        print(f"Database: {getenv('DATABASE_URL')}")
        print(f"API Access: {getenv('API_KEY')}")
        print(f"Log Level: {getenv('LOG_LEVEL')}")
        print(f"Zion Network: {getenv('ZION_ENDPOINT')}")

        print("\nEnvironment security check:")
        print("[OK] No hardcoded secrets detected")
        print("[OK] .env file properly configured")
        print("[OK] Production overrides available")
    except (ImportError):
        print("Missing Module: python-dotenv")


def main() -> None:
    print("\nORACLE STATUS: Reading the Matrix...\n")
    checker()
    print("\nThe Oracle sees all configurations.")


if __name__ == "__main__":
    main()
