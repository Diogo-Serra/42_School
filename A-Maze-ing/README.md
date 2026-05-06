# A-Maze-ing

This project is present here: https://github.com/Diogo-Serra/A-Maze-ing

---

## Description

A-Maze-ing is a Python maze generator project for 42 Core curriculum that procedurally creates fully connected, solvable mazes using a Depth-First Search (DFS) algorithm. The program supports graphical display, step-through visualization, seed-based reproducibility, and configuration via a settings file.

---

## Instructions

### Requirements

- Python 3.x
- pip
- pydantic
- flake8
- mypy

### Installation

```bash
git clone git@github.com:Diogo-Serra/A-Maze-ing.git
cd A-Maze-ing
make install
make run
```

### Execution

Run with a seed (optional):
```bash
python a-maze-ing.py [seed]
```

Run with a settings file:
```bash
python a-maze-ing.py config.txt
```

---

## Settings File Format

The settings file must follow this structure:

```
WIDTH=int
HEIGHT=int
ENTRY=tuple
EXIT=tuple
OUTPUT_FILE=maze.txt
PERFECT=bool
SEED=int
```

All fields are required.

---

## Maze Generation Algorithm

The maze is generated using a **Depth-First Search (DFS)** algorithm with recursive backtracking:

1. Start at a random cell and mark it as visited.
2. Randomly choose an unvisited neighbouring cell, carve a passage to it, and move there.
3. If no unvisited neighbours exist, backtrack to the previous cell.
4. Repeat until all cells have been visited.

This guarantees a fully connected, solvable maze with exactly one path between any two cells.

### Why DFS?

The team decided on DFS because it is simple to implement, produces long winding corridors (visually interesting and challenging), and guarantees a perfect maze (no loops and no isolated regions). Its recursive nature also maps naturally to Python. This algorithm can still be revisited and changed.

---

## Reusable Components

- **Maze class** (`classes.py`) - General purpose maze class, takes validated data and handles generation and output.

- **Settings class** (`classes.py`) - Pydantic-based validation model, easily adapted to validate any structured config data beyond mazes.

- **Parser** (`parser.py`) - Handles config file reading, class instantiation and all error catching through a versatile entry point `load_settings()`.

---

## Team & Project Management

### Roles

| Member | Role |
|---|---|
| [Diogo Serra](https://github.com/Diogo-Serra) | Settings parser, pathfinder
| [Pedro Pinhão](https://github.com/Retr02k) | Core algorithm, graphics

### Planning

Initial planned timeline:

Week 1:

    Project setup, algorithm research
    Settings parsing, maze flow and menus

Week 2:

    Core maze generation & Pathfinder
    Graphical display and visualization


### What Worked Well & What Could Be Improved

**Worked well:**
    ...

**Could be improved:**
    ...

### Tools Used

- **Version Control**: Git, GitHub
- **Core Development**: Python, pip, venv
- **Validation & Quality**: pydantic, flake8, mypy
- **Environment & Editor**: Linux, VS Code
- **Shells**: bash, zsh

---

## Resources

- DFS maze generation: https://en.wikipedia.org/wiki/Maze_generation_algorithm
- Python `random` module: https://docs.python.org/3/library/random.html
- Python documentation: https://docs.python.org/3/
- Pydantic documentation: https://docs.pydantic.dev/
- pip documentation: https://pip.pypa.io/en/stable/
- flake8 documentation: https://flake8.pycqa.org/
- W3Schools Python references: https://www.w3schools.com/python/
- GeeksforGeeks DFS references: https://www.geeksforgeeks.org/depth-first-search-or-dfs-for-a-graph/

### AI Usage

AI tools were used for research support, concept clarification, and visual explanations to better understand maze generation logic.
AI was also used to support with markdown language on this README file.

No code was generated with AI; implementation, decisions and code were written by the team.
