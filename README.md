# Maze Solver

An interactive maze/pathfinding visualizer built with Pygame. You can place a start node, destination node, and obstacles on a grid, then watch different algorithms explore the space and produce a path.

## Project Overview

This project demonstrates and compares pathfinding behavior in a visual, grid-based environment. It is designed as a hands-on sandbox for understanding how A*, Dijkstra, and DFS traverse nodes under the same map conditions.

## Features

- Interactive grid editor for start, destination, and obstacles
- Pathfinding visualization with:
  - A* search
  - Dijkstra
  - Depth-First Search (DFS)
- Real-time exploration rendering (searched nodes + final path)
- Adjustable solving speed while an algorithm is running
- Random mode for repeatedly generating and solving scenarios
- In-app menu and keyboard controls

## Architecture / Structure

Core modules:

- `Main.py` - Application entry point, initializes maze + graphics
- `Grafics.py` - UI/event loop, controls handling, rendering, and solver orchestration
- `Maze.py` - Grid model and node management (map creation, start/destination/path/obstacles)
- `Node.py` - Node state and distance logic used by algorithms
- `PathFindingAlgorithm.py` - Search implementations and per-step solving cycle

Data flow (high level):

1. `Main` creates a `Maze` and initializes `Graphics`.
2. `Graphics` processes user input and starts a selected algorithm.
3. `PathFindingAlgorithm` runs incrementally (`solutionCycle`) and updates node state.
4. `Graphics` renders searched nodes and final path on each frame.

## Build & Run Instructions

### Prerequisites

- Python 3.9+ recommended
- A desktop environment (Pygame window required)

### Setup

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### Run

```bash
python Main.py
```

### Controls

- `S` + mouse: place start
- `D` + mouse: place destination
- `O` + mouse: place obstacles
- `1`: solve with A*
- `2`: solve with Dijkstra
- `3`: solve with DFS
- `R`: toggle random mode
- `+` / `-`: adjust obstacle draw size or solving speed (context-dependent)
- `Esc`: clear obstacles (if present) or open menu

## Screenshots

### 1) Interactive setup

![Maze setup view](https://files.fm/thumb_show.php?i=yw4fkmb2g)

This view shows the editing phase where you place the start node, destination node, and obstacles before running an algorithm.

### 2) Search in progress

![Search visualization](https://files.fm/thumb_show.php?i=jcky6bng6)

Here the solver is actively exploring the grid. The searched-node coloring helps illustrate how the algorithm expands through the maze.

### 3) Final path result

![Solved path result](https://files.fm/thumb_show.php?i=mcpr5htma)

This screenshot highlights the completed path from start to destination after the selected algorithm finishes.

## Testing

This repository currently has no automated test suite.

Suggested manual checks:

- Verify each algorithm (`1`, `2`, `3`) finds a path on an empty grid
- Add obstacle patterns and confirm expected rerouting
- Confirm behavior when no valid path exists
- Confirm speed controls and random mode behavior

## Project Context

This is an educational visualization project focused on algorithm behavior rather than production-grade pathfinding APIs. The code is organized for readability and interactive experimentation, making it useful for learning, demos, and iterative algorithm tuning.
