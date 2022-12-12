import pandas as pd
import numpy as np
from utils import get_puzzle_input

EXAMPLE_INPUT = """Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi"""
EXAMPLE_SOLUTION_A = 31
EXAMPLE_SOLUTION_B = 29

ELEVATION = "SabcdefghijklmnopqrstuvwxyzE"


def find_dist(puzzle_input):
    grid = np.stack([[ELEVATION.index(col) for col in row] for row in puzzle_input.split("\n")]).astype(int)
    start = tuple(np.argwhere(grid == 0)[0])
    end = tuple(np.argwhere(grid == len(ELEVATION) - 1)[0])
    grid[start] = 1  # S actually has the same elevation as a
    grid[end] = len(ELEVATION) - 2  # E actually has the same elevation as z
    dist = np.full_like(grid, -1)
    dist[end] = 0

    def get_neighbors(rc):
        r, c = rc
        cand = [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]
        return [(r, c) for (r, c) in cand if 0 <= r < grid.shape[0] and 0 <= c < grid.shape[1]]

    def add_neigh_dist(rc):
        new_neigh = []
        for neigh in get_neighbors(rc):
            if (dist[neigh] == -1 or dist[neigh] > dist[rc] + 1) and grid[neigh] + 1 >= grid[rc]:
                dist[neigh] = dist[rc] + 1
                new_neigh.append(neigh)
        return new_neigh

    new_neigh = [end]
    while new_neigh:
        neigh = []
        for rc in new_neigh:
            neigh += add_neigh_dist(rc)
        new_neigh = set(neigh)

    return grid, dist, start


def solve_a(puzzle_input):
    grid, dist, start = find_dist(puzzle_input)
    return dist[start]


def solve_b(puzzle_input):
    grid, dist, start = find_dist(puzzle_input)
    return min([x for x in dist[np.where(grid == 1)] if x != -1])


if __name__ == "__main__":
    puzzle_input = get_puzzle_input(__file__)

    assert solve_a(EXAMPLE_INPUT) == EXAMPLE_SOLUTION_A
    print(solve_a(puzzle_input))

    assert solve_b(EXAMPLE_INPUT) == EXAMPLE_SOLUTION_B
    print(solve_b(puzzle_input))
