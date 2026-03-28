#!/usr/bin/env python3
import sys


def ft_stream_management() -> None:
    print("=== CYBER ARCHIVES - COMMUNICATION SYSTEM ===\n")
    sys.stdout.write("Input Stream active. Enter archivist ID: ")
    sys.stdout.flush()
    archivist_id: str = sys.stdin.readline().strip()
    sys.stdout.write("Input Stream active. Enter status report: ")
    sys.stdout.flush()
    status_report: str = sys.stdin.readline().strip()
    sys.stdout.write("\n[STANDARD] Archive status from "
                     + archivist_id + ": " + status_report + "\n")
    sys.stderr.write("[ALERT] System diagnostic: Communication"
                     " channels verified\n")
    sys.stdout.write("[STANDARD] Data transmission complete\n")
    sys.stdout.write("\nThree-channel communication test successful.\n")


ft_stream_management()
