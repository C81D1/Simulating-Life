# Life Simulation - Conways Game of Life

A Python implementation of Conway's Game of Life — a zero-player cellular automaton where a grid of cells evolves over time according to a few simple rules.

## What It Does

The program simulates generations of cells on a 2D grid. Each cell is either **alive** or **dead**, and on every tick each cell's fate is decided by how many of its 8 neighbors are alive. From these trivial rules, surprisingly complex behavior emerges — oscillating shapes, spaceships that glide across the grid, and chaotic patterns that grow and settle.

## Rules

For every cell, applied simultaneously each generation:

**If the cell is alive:**
- 0 or 1 live neighbors → dies (underpopulation)
- 2 or 3 live neighbors → survives
- 4 or more live neighbors → dies (overpopulation)

**If the cell is dead:**
- Exactly 3 live neighbors → becomes alive (birth)
- Any other count → stays dead

Every cell updates at the same time, based only on the previous generation. A fully dead grid stays dead forever.

## Features

- Grid-based simulation with configurable size
- Random starting state (adjustable density)
- Preset patterns (glider, blinker, pulsar, glider gun, R-pentomino)
- Terminal or graphical rendering
- Step-by-step or continuous evolution

## How It Works

1. Maintain two grids: current and next.
2. For each cell, count live neighbors from the current grid.
3. Apply the rules and write results to the next grid.
4. Swap grids and render.
5. Repeat.

## Usage

```
run the program
optionally pick a starting pattern or let it randomize
watch the generations evolve
```

## Why It's Interesting

Despite having no players and only four rules, the Game of Life is **Turing-complete** — it can theoretically compute anything a computer can. It's a classic example of emergence: simple local rules producing complex global behavior.

## Requirements

- Python 3.x (or your language of choice)
- Optional: pygame or similar for graphical rendering

## License

Free to use and modify.