# Codexion

This project is present here: https://github.com/Diogo-Serra/Codexion

---

A concurrent coder simulation in which multiple coders work around a circular co-working hub and share a limited set of USB dongles connected to a central Quantum Compiler. Each coder alternates between compiling, debugging, and refactoring, while respecting strict resource and timing constraints.

The simulation models the classic resource-sharing problem using threads, synchronization primitives, and carefully coordinated access to shared dongles. Every coder must acquire two adjacent dongles before compiling, release them after compilation, and continue through the debugging and refactoring phases before attempting to compile again.

The program validates all mandatory parameters, supports FIFO and Earliest Deadline First (EDF) dongle scheduling policies, and enforces dongle cooldown periods. It also monitors compilation deadlines to detect coder burnout and stops successfully once every coder has completed the required number of compilations.

Throughout the simulation, each coder's state changes are logged with timestamps, including dongle acquisition, compiling, debugging, refactoring, and burnout events. The implementation focuses on preventing deadlocks, avoiding data races, respecting timing limits, and ensuring that output messages remain clear and correctly formatted.