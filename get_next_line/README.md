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

The implementation uses a **static buffer** that persists between function calls, acting as a sliding window that stores leftover data from previous reads.

### Main Components

#### 1. **`get_next_line(int fd)`** - Entry Point & Main Loop
- **Input Validation**: Checks `fd >= 0` and `BUFFER_SIZE >= 1`
- **Static Buffer**: Uses `buffer[BUFFER_SIZE + 1]` to persist data between calls
- **Loop Condition**: Continues while `bytes > 0` OR `buffer[0]` contains data
  - This ensures leftover data from previous reads is processed
  - Allows handling lines that span multiple reads

#### 2. **Read Phase**
- **Conditional Reading**: Only reads when buffer is empty (`!buffer[0]`)
  - Prevents overwriting unprocessed data
  - Reads up to `BUFFER_SIZE` bytes from `fd`
  - Buffer is automatically null-terminated due to `[BUFFER_SIZE + 1]` size
- **Error Handling**: If `read()` returns `-1`:
  - Calls `clean_buffer(buffer)` to clear static state
  - Frees accumulated `line`
  - Returns `NULL`
- **EOF Detection**: If `read()` returns `0` and buffer is empty:
  - Returns current `line` (may be `NULL` if nothing accumulated)

#### 3. **Line Building Phase**
- **`ft_strnjoin(line, buffer)`**: Appends buffer content to line
  - Takes existing `line` (or `NULL`) and joins with buffer content
  - Returns newly allocated string containing both parts
  - Old `line` is freed inside `ft_strnjoin()`
- **Allocation Check**: If `ft_strnjoin()` returns `NULL`:
  - Calls `clean_buffer(buffer)` to clear static state
  - Returns `NULL` (no need to free `line` as it was freed in `ft_strnjoin`)

#### 4. **Buffer Management**
- **`clean_buffer(buffer)`**: Called after each join
  - Moves remaining content (after newline) to start of buffer
  - Clears the rest of the buffer with null bytes
  - Preserves data for next iteration/call
- **Newline Detection**: Uses `ft_strchr(line, '\n')` after cleaning
  - If found: breaks loop and returns complete line (including `\n`)
  - If not found: continues reading more data

### Memory Management

- **Static buffer** survives function returns, maintaining partial lines
- **Dynamic line** grows with each `ft_strnjoin()` call:
  - Old allocation is freed internally
  - New allocation holds combined content
- **Buffer state** is cleaned after processing to preserve only unread data
- **Error cleanup**: Both static buffer and dynamic line are cleaned/freed on errors

### Edge Cases Handled

- **Invalid input**: `fd < 0` or `BUFFER_SIZE < 1` returns `NULL`
- **Read errors**: Cleans buffer and frees line before returning `NULL`
- **Empty files**: Returns `NULL` (no data accumulated)
- **No trailing newline**: Returns last line without `\n`
- **Lines longer than `BUFFER_SIZE`**: Accumulated across multiple reads
- **Multiple consecutive newlines**: Each returned as separate line on subsequent calls
- **Multiple file descriptors**: Each `fd` uses its own call context but shares the same static buffer
