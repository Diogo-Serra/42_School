<p align="center">
  <img src="https://github.com/Diogo-Serra/42-project-badges/blob/main/covers/cover-ft_printf.png" alt="Banner">
</p>

---

# 42 School Project - ft_printf

`ft_printf` is a 42 School project that requires recreating the standard `printf()` function with basic format conversions.

**Goal**: Print formatted output using a variable number of arguments and return the total character count.

**Key Concepts**: Variadic functions, format specifiers, type conversion, `va_list`, `va_start`, `va_arg`, `va_end`.

---

## Function

```c
int ft_printf(const char *format, ...);
```

---

## Supported Conversions

| Specifier | Description | Type |
|-----------|-------------|------|
| `%c` | Single character | `char` |
| `%s` | String | `char *` |
| `%p` | Pointer address in hexadecimal | `void *` |
| `%d` | Signed decimal integer | `int` |
| `%i` | Signed decimal integer | `int` |
| `%u` | Unsigned decimal integer | `unsigned int` |
| `%x` | Unsigned hexadecimal (lowercase) | `unsigned int` |
| `%X` | Unsigned hexadecimal (uppercase) | `unsigned int` |
| `%%` | Literal percent sign | - |

---

## Implementation Logic

### Core Algorithm

The implementation uses **variadic functions** (`va_list`) to handle a variable number of arguments and dispatches formatting based on conversion specifiers.

### Main Components

#### 1. **`ft_printf(const char *src, ...)`** - Entry Point
- Initializes a `va_list` to access variable arguments
- Iterates through the format string character by character
- When `%` is encountered:
  - Calls `print_handler()` with the next character as the format specifier
  - Increments the character count by the return value
- Regular characters are written directly to stdout
- Returns the total number of characters printed
- Calls `va_end()` to clean up the argument list

#### 2. **`print_handler(va_list pargs, const char flag)`** - Format Dispatcher
- Routes execution based on the format specifier:
  - **Character types** (`c`, `s`, `%`): delegates to `print_chr()`
  - **Numeric types** (`d`, `i`, `u`, `x`, `X`): delegates to `print_nbr()`
  - **Pointer type** (`p`): handles directly
- **Pointer handling (`%p`)**:
  - Extracts `void *` argument and casts to `unsigned long`
  - If `NULL`: prints `"(nil)"`
  - Otherwise: prints `"0x"` prefix followed by hexadecimal address
- Returns the number of characters printed

#### 3. **`print_chr(va_list pargs, const char flag)`** - Character/String Handler
- **`%c`**: Extracts `int` argument (promoted from `char`), writes single character
- **`%s`**: Extracts `char *` argument
  - If `NULL`: prints `"(null)"`
  - Otherwise: calculates string length and writes entire string
- **`%%`**: Writes literal `%` character
- Returns the number of characters written

#### 4. **`print_nbr(va_list pargs, const char flag)`** - Numeric Handler
- **`%d` / `%i`**: Extracts `int`, converts to decimal base
- **`%u`**: Extracts `unsigned int`, converts to decimal base
- **`%x`**: Extracts `unsigned int`, converts to lowercase hexadecimal
- **`%X`**: Extracts `unsigned int`, converts to uppercase hexadecimal
- Uses helper function `ft_putnbr_base()` with appropriate base strings:
  - `DECIMAL`: `"0123456789"`
  - `LOWER_HEX`: `"0123456789abcdef"`
  - `UPPER_HEX`: `"0123456789ABCDEF"`
- Returns the number of characters printed

### Helper Function

#### **`ft_putnbr_base(long nbr, const char *base, int base_len)`**
- Converts and prints a number in the specified base
- Handles negative numbers for signed integers
- Recursively processes digits
- Returns the total character count

---

## Memory Management

- **No dynamic allocation**: all output is written directly to stdout
- **Safe va_list handling**: `va_end()` is always called before returning
- **NULL pointer safety**: `%s` checks for `NULL` strings, `%p` checks for `NULL` pointers

---

## Edge Cases Handled

- Empty format string
- Consecutive `%` characters (`%%`)
- NULL string pointers (`%s` with `NULL` → prints `"(null)"`)
- NULL pointers (`%p` with `NULL` → prints `"(nil)"`)
- Maximum/minimum integer values
- Zero values for all numeric types
- Uppercase vs lowercase hexadecimal distinction

---

## Return Value

Returns the **total number of characters printed**, matching the behavior of the standard `printf()`.
