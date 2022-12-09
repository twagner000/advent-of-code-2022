import pandas as pd
import numpy as np
from utils import get_puzzle_input

EXAMPLE_INPUT = """30373
25512
65332
33549
35390"""
EXAMPLE_SOLUTION_A = 21
EXAMPLE_SOLUTION_B = 8


def prepare_grid(puzzle_input):
    return np.stack([[int(col) for col in row] for row in puzzle_input.split('\n')])


def get_views(grid, r, c):
    return [
        grid[0:r, c][::-1],  # up
        grid[r + 1:grid.shape[0], c],  # below
        grid[r, 0:c][::-1],  # left
        grid[r, c + 1:grid.shape[1]],  # right
    ]


def solve_a(puzzle_input):
    grid = prepare_grid(puzzle_input)
    visible = np.ones_like(grid)
    for r in range(1, grid.shape[0] - 1):
        for c in range(1, grid.shape[1] - 1):
            val = grid[r, c]
            for view in get_views(grid, r, c):
                if val > view.max():
                    break
            else:
                visible[r, c] = 0
    return visible.sum()


def solve_b(puzzle_input):
    grid = prepare_grid(puzzle_input)
    score = np.ones_like(grid)
    for r in range(grid.shape[0]):
        for c in range(grid.shape[1]):
            val = grid[r, c]
            for view in get_views(grid, r, c):
                view_score = 0
                for v in view:
                    view_score += 1
                    if v >= val:
                        break
                score[r, c] *= view_score
    return score.max()


if __name__ == "__main__":
    puzzle_input = get_puzzle_input(__file__)

    assert solve_a(EXAMPLE_INPUT) == EXAMPLE_SOLUTION_A
    print(solve_a(puzzle_input))

    assert solve_b(EXAMPLE_INPUT) == EXAMPLE_SOLUTION_B
    print(solve_b(puzzle_input))
