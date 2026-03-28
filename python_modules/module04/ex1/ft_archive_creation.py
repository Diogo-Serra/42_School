#!/usr/bin/env python3
from typing import IO


def ft_archive_creation() -> None:
    data_tosave: list[str] = [
        "[ENTRY 001] New quantum algorithm discovered\n",
        "[ENTRY 002] Efficiency increased by 347%\n",
        "[ENTRY 003] Archived by Data Archivist trainee",
    ]
    print("=== CYBER ARCHIVES - PRESERVATION SYSTEM ===\n")
    print("Initializing new storage unit: new_discovery.txt")
    f: IO[str] = open("new_discovery.txt", "w")
    print("Storage unit created successfully...\n")
    print("Inscribing preservation data...")
    for data in data_tosave:
        f.write(data)
        print(data, end='')
    print("\n\nData inscription complete. Storage unit sealed.")
    file_name: str = f.name
    f.close()
    print(f"Archive '{file_name}' ready for long-term preservation.")


ft_archive_creation()
