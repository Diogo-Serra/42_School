*This project has been created as part of the 42 curriculum by diosoare.*

<p align="center">
  <img src="https://github.com/Diogo-Serra/42-project-badges/blob/main/covers/cover-push_swap.png" alt="Banner">
</p>

---

## Description

`push_swap` is a sorting algorithm project that challenges you to sort data on a stack with a limited set of instructions and using the lowest possible number of moves. The project involves implementing an efficient sorting algorithm using two stacks (A and B) and a specific set of operations.

**Goal**: Sort a stack of integers in ascending order (smallest number at the top) using the minimum number of operations possible.

The project involves:
- Parsing and validating input (integers with no duplicates)
- Implementing stack operations (swap, push, rotate, reverse rotate)
- Developing an efficient sorting algorithm
- Optimizing for performance (number of moves)

For small stacks (≤5 elements), a hardcoded solution is used. For larger stacks, the implementation uses a **Radix Sort algorithm specifically adapted for stack operations**. The algorithm leverages the limited instruction set (push, rotate, swap) to sort efficiently: first, each number is **indexed** according to its position in sorted order (smallest = 0, next = 1, etc.), transforming arbitrary integers into a sequential range (0 to n-1). Then, using only stack operations, the algorithm sorts these indices by examining their binary representation bit by bit—pushing elements to stack B or keeping them in stack A based on each bit value, effectively sorting through binary place values. This stack-based adaptation of radix sort achieves excellent performance while respecting the operational constraints of the problem.

**Key Concepts**: Algorithm optimization, data structures (stacks), complexity analysis, binary operations, sorting algorithms.

---

## Instructions

### Compilation

To compile the project, run:

```bash
make
```

This will:
1. Compile the libft library (located in `libft/`)
2. Compile all source files from `src/`
3. Generate the `push_swap` executable

### Cleaning

```bash
make clean    # Remove object files
make fclean   # Remove object files and executable
make re       # Recompile everything
```

### Usage

Run the program with a list of integers as arguments:

```bash
./push_swap 3 2 1 5 4
./push_swap "3 2 1 5 4"
./push_swap 42 1 -17 8 0
```

The program will output the list of operations needed to sort the stack.

### Validation with Checker

The project includes a `checker_linux` binary to validate the sorting:

```bash
ARG="3 2 1 5 4"; ./push_swap $ARG | ./checker_linux $ARG
```

If the stack is sorted correctly, the checker will output `OK`. If not, it will output `KO`.

### Examples

```bash
# Sort 3 numbers
$ ./push_swap 2 1 3
sa
ra

# Sort 5 numbers
$ ./push_swap 2 1 3 6 5 8
pb
pb
sa
pa
pa
```

---

## Allowed Operations

The program can only use the following operations to sort the stack:

| Operation | Description |
|-----------|-------------|
| `sa` | Swap first 2 elements of stack A |
| `sb` | Swap first 2 elements of stack B |
| `ss` | `sa` and `sb` at the same time |
| `pa` | Push top element from B to A |
| `pb` | Push top element from A to B |
| `ra` | Rotate stack A up (first element becomes last) |
| `rb` | Rotate stack B up |
| `rr` | `ra` and `rb` at the same time |
| `rra` | Reverse rotate stack A (last element becomes first) |
| `rrb` | Reverse rotate stack B |
| `rrr` | `rra` and `rrb` at the same time |

---

## Algorithm Overview

### Small Stacks (2-5 elements)

For stacks with 2 to 5 elements, a hardcoded optimal solution is implemented that checks all possible configurations and applies the minimum number of moves.

### Large Stacks (Radix Sort)

For stacks with more than 5 elements, the implementation uses a modified Radix Sort algorithm:

1. **Indexing**: Assign each number an index based on its position in sorted order (smallest = 0)
2. **Binary Sorting**: Process numbers bit by bit (from LSB to MSB)
3. **For each bit position**:
   - Push numbers with bit = 0 to stack B
   - Keep numbers with bit = 1 in stack A
   - Push everything back from B to A
4. After processing all bits, stack A is sorted

This approach provides excellent performance:
- **Time Complexity**: O(n × log n)
- **Space Complexity**: O(1) auxiliary space (only uses 2 stacks)

---

## Project Structure

```
push_swap/
├── Makefile           # Build configuration
├── push_swap.h        # Header file with structures and function prototypes
├── README.md          # This file
├── checker_linux      # Validation binary
├── libft/             # Custom C library
│   └── ...
└── src/               # Source files
    ├── main.c         # Entry point and main sorting logic
    ├── parsing.c      # Input parsing and validation
    ├── parsing_utils.c # Parsing helper functions
    ├── operations.c   # Stack operations implementation
    ├── utils.c        # Stack utility functions
    ├── error_handling.c # Error management and memory cleanup
    ├── sort_small.c   # Optimized sorting for small stacks (≤5)
    └── radix_sort.c   # Radix sort implementation for large stacks
```

---

## Resources

### Documentation & Tutorials
- [Github - push_swap](https://github.com/gkomba/Push_Swap_Tester)
- [Stack Data Structure](https://42-cursus.gitbook.io/guide/2-rank-02/push_swap)
- [Radix Sort Algorithm](https://www.geeksforgeeks.org/dsa/radix-sort/)
- [Sorting Algorithm Complexity](https://www.bigocheatsheet.com/)

### Articles & Guides
- [Push_swap: The least amount of moves with two stacks](https://medium.com/@jamierobertdawson/push-swap-the-least-amount-of-moves-with-two-stacks-d1e76a71789a)
- [Sorting Algorithms Visualized](https://visualgo.net/en/sorting)

### AI Usage
**AI tools were used in this project for the following purposes:**
- **Code review and debugging**: Used to identify potential memory leaks and edge cases in parsing logic
- **Algorithm optimization**: Consulted for best practices in implementing radix sort for stack-based data structures
- **Documentation**: Assisted in structuring this README and explaining algorithm complexity
- **Code explanations**: Used to understand certain bitwise operations used in radix sort

**AI was NOT used for:**
- Writing the core algorithm implementation from scratch
- Solving the project's main challenges
- Generating the sorting logic

All core functionality, algorithm design, and problem-solving were done independently, with AI serving as a supplementary learning and debugging tool.

---

## Performance

The implementation achieves the following performance benchmarks:

- **3 numbers**: ≤3 operations
- **5 numbers**: ≤12 operations
- **100 numbers**: ≤1084 operations (excellent: <700, good: <900, acceptable: <1100)
- **500 numbers**: ≤6784 operations (excellent: <5500, good: <7000, acceptable: <11500)

**Why are operations count consistent?**

The radix sort algorithm has predictable performance because it depends on the number of bits required to represent the largest index:
- **100 numbers** require 7 bits (since 2^7 = 128 > 100)
- **500 numbers** require 9 bits (since 2^9 = 512 > 500)

For each bit level, the algorithm processes all numbers (push some to B, then push back to A), resulting in approximately **n × number_of_bits** operations. This makes the operation count deterministic and independent of the input values—only the size of the input matters. This is why with the same number of elements, you'll always get roughly the same number of operations, regardless of which specific numbers are being sorted.

---

## Author

**diosoare** - 42 Lisboa
- GitHub: [@Diogo-Serra](https://github.com/Diogo-Serra)
