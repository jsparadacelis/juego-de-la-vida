# Juego de la Vida (Conway's Game of Life)

A Python implementation of Conway's Game of Life, a cellular automaton devised by mathematician John Horton Conway in 1970.

## Description

The Game of Life is a zero-player game, meaning that its evolution is determined by its initial state, requiring no further input. One interacts with the Game of Life by creating an initial configuration and observing how it evolves.

### Rules

The universe of the Game of Life is an infinite, two-dimensional orthogonal grid of square cells, each of which is in one of two possible states: live (1) or dead (0). Every cell interacts with its eight neighbors. At each step in time, the following transitions occur:

1. Any live cell with fewer than two live neighbors dies (underpopulation)
2. Any live cell with two or three live neighbors lives on to the next generation
3. Any live cell with more than three live neighbors dies (overpopulation)
4. Any dead cell with exactly three live neighbors becomes a live cell (reproduction)

## Requirements

- Python 3.8 or higher
- No external dependencies required (uses only standard library)

## How to Play

### Running the Game

1. Navigate to the project directory:
   ```bash
   cd /path/to/juego-de-la-vida
   ```

2. Run the game:
   ```bash
   python app/juego.py
   ```

3. The game will start with a predefined initial pattern and will automatically evolve according to Conway's rules.

4. To stop the game, press `Ctrl+C`.

### Initial Pattern

The game starts with a simple pattern called a "glider" that moves across the grid:
```
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 1 0 0 0 0
0 0 0 0 1 0 0 0 0 0
0 0 0 0 1 1 1 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
```

### Customizing the Initial Pattern

To create your own initial pattern, modify the `INITIAL_MATRIX` variable in `app/juego.py`:

- `0` represents a dead cell
- `1` represents a live cell

You can create different patterns like:
- **Still lifes**: Patterns that don't change (e.g., block, beehive)
- **Oscillators**: Patterns that return to their initial state after a finite number of generations (e.g., blinker, toad)
- **Spaceships**: Patterns that translate themselves across the board (e.g., glider, lightweight spaceship)

## Project Structure

```
juego-de-la-vida/
├── app/
│   ├── __init__.py
│   ├── juego.py          # Main game implementation
│   └── test_juego.py     # Test file
├── .gitignore
└── README.md
```

## Features

- Console-based visualization
- Automatic evolution with configurable speed (0.5 seconds between generations)
- Proper boundary handling for edge cases
- Clean terminal clearing between generations
- Graceful exit with Ctrl+C

## Development

### Running Tests

```bash
python -m pytest app/test_juego.py
```

### Code Structure

- `print_matrix()`: Displays the current state of the grid
- `calculate_alive_neighbors()`: Counts live neighbors for a given cell position
- `generate_new_matrix()`: Applies Conway's rules to generate the next generation
- `main()`: Main game loop with display and evolution

## License

This project is open source and available under the MIT License.

## About Conway's Game of Life

Conway's Game of Life demonstrates how complex behaviors can emerge from simple rules. Despite its simplicity, the Game of Life is Turing complete, meaning it can simulate any computer algorithm. It has been a subject of interest for mathematicians, computer scientists, and enthusiasts for decades.
