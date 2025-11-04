<div align="center">

<img src="https://github.com/ayogun/42-project-badges/blob/main/covers/cover-get_next_line-bonus.png?raw=true"/>

# 42 School Project - get_next_line

## Overview

`get_next_line` is a 42 School project that requires writing a function to read a line from a file descriptor, one at a time.



---

**Goal**: Return one line per call, ending with `\n` (or until EOF).

**Key Concepts**: Static variables, buffer management, `read()`, memory allocation.

**BUFFER_SIZE**: Defined at compile time (`-D BUFFER_SIZE=n`).

---

## Function

```c
char *get_next_line(int fd);
```
