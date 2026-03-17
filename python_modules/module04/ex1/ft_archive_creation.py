#!/usr/bin/env python3


def ft_archive_creation():
    data_tosave = [
        "[ENTRY 001] New quantum algorithm discovered\n",
        "[ENTRY 002] Efficiency increased by 347%\n",
        "[ENTRY 003] Archived by Data Archivist trainee",
    ]
    print("=== CYBER ARCHIVES - PRESERVATION SYSTEM ===\n")
    f = open("new_discovery.txt", "wt")
    for data in data_tosave:
        f.write(data)
    f.close()


ft_archive_creation()
