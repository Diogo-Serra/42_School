<p align="center">
  <img src="https://github.com/Diogo-Serra/42-project-badges/blob/main/covers/cover-push_swap.png" alt="Banner">
</p>

---

# 42 School Project - push_swap

`push_swap` is a 42 School project that requires implementing a sorting algorithm using two stacks and a limited set of operations.

**Goal**: Sort a stack of integers in ascending order using the minimum number of operations.

**Key Concepts**: Algorithm optimization, stack manipulation, complexity analysis, instruction sets.

---

## The Challenge

- **Stack A**: Contains random integers (no duplicates)
- **Stack B**: Empty at start
- **Objective**: Sort stack A in ascending order (smallest at top)

---

## Allowed Operations

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
