<p align="center">
  <img src="https://github.com/Diogo-Serra/42-project-badges/blob/main/covers/cover-get_next_line.png" alt="Banner">
</p>

---

# 42 School Project - get_next_line

`get_next_line` is a 42 School project that requires writing a function to read a line from a file descriptor, one at a time.

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

The implementation uses a **static buffer** that persists between function calls, allowing the function to maintain state and handle lines that span multiple reads.

### Main Components

#### 1. **`get_next_line(int fd)`** - Entry Point
- Validates input (`fd >= 0` and `BUFFER_SIZE > 0`)
- Uses a static buffer array `[BUFFER_SIZE + 1]` to persist data between calls
- Calls `gnl_handler()` to process the file descriptor and buffer

#### 2. **`gnl_handler(int fd, char *buffer)`** - Buffer Management
- Duplicates the static buffer content into dynamic storage using `ft_strdup()`
- Reads from `fd` in chunks of `BUFFER_SIZE` bytes
- Continues reading until:
  - A newline character (`\n`) is found in storage
  - End of file is reached (`bytes == 0`)
  - An error occurs (`bytes < 0`)
- Appends each read chunk to storage using `ft_strjoin()`
- Null-terminates the buffer after each read
- If newline found: calls `gnl_extract_line()` to separate line from remainder
- If EOF reached without newline: returns entire storage and clears buffer

#### 3. **`gnl_extract_line(char *storage, char *buffer)`** - Line Extraction & Storage Update
- Locates the first newline character using `ft_strchr()`
- Calculates line length (including `\n`)
- Allocates and copies the line (from start to newline inclusive)
- Updates the static buffer with remaining content after the newline
- Frees the storage
- Returns the extracted line

### Memory Management

- **Static buffer** persists between calls to maintain partial lines
- **Dynamic storage**: temporary storage is allocated and freed within each call
- **Buffer reuse**: static buffer is updated with leftover content after line extraction
- **Automatic cleanup**: storage is freed before returning
- **Error handling**: all allocations are checked; on failure, storage is freed and `NULL` is returned

### Edge Cases Handled

- Invalid file descriptor (`fd < 0`)
- Invalid buffer size (`BUFFER_SIZE <= 0`)
- Read errors (returns `NULL` and cleans up)
- Empty files (returns `NULL`)
- Files without trailing newline (returns last line without `\n`)
- Lines longer than `BUFFER_SIZE`
- Multiple consecutive newlines
