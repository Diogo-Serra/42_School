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

---


## Implementation Logic

### Core Algorithm

The implementation uses a **static storage buffer** that persists between function calls, allowing the function to maintain state and handle lines that span multiple reads.

### Main Components

#### 1. **`get_next_line(int fd)`** - Entry Point
- Validates input (`fd >= 0` and `BUFFER_SIZE > 0`)
- Allocates a temporary buffer for reading
- Calls `reading()` to fill the static storage
- Extracts the current line with `load_line()`
- Trims the storage to remove the returned line with `trim_storage()`

#### 2. **`reading(int fd, char **storage, char *buffer)`** - Buffer Management
- Reads from `fd` in chunks of `BUFFER_SIZE` bytes
- Continues reading until:
  - A newline character (`\n`) is found in storage
  - End of file is reached (`bytes_read == 0`)
  - An error occurs (`bytes_read < 0`)
- Appends each read chunk to the static storage using `ft_strjoin_free()`
- Null-terminates the buffer after each read

#### 3. **`load_line(char *storage)`** - Line Extraction
- Locates the first newline character in storage
- If found: returns substring from start to newline (inclusive)
- If not found: returns the entire storage content (EOF case)
- Returns `NULL` if storage is empty

#### 4. **`trim_storage(char *storage)`** - Storage Cleanup
- Finds the newline character position
- Extracts remaining content after the newline
- Frees the old storage
- Returns the new storage (or `NULL` if no content remains)

#### 5. **`ft_strjoin_free(char *s1, char const *s2)`** - Memory Optimization
- Joins two strings and frees the first one
- Reduces memory allocations by reusing the storage pointer
- Uses `ft_calloc()` for automatic null-termination

### Memory Management

- **Static variable** persists between calls to maintain partial lines
- **Automatic cleanup**: storage is freed when empty or on error
- **Safe freeing**: always frees old storage before reassigning
- **Error handling**: all allocations are checked; on failure, storage is freed and `NULL` is returned

### Edge Cases Handled

- Invalid file descriptor (`fd < 0`)
- Invalid buffer size (`BUFFER_SIZE <= 0`)
- Read errors (returns `NULL` and cleans up)
- Empty files
- Files without trailing newline
- Lines longer than `BUFFER_SIZE`
