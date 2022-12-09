import re
import pandas as pd
import numpy as np
from utils import get_puzzle_input

EXAMPLE_INPUT = """R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2"""
EXAMPLE_SOLUTION_A = 13
EXAMPLE_SOLUTION_B = 1
EXAMPLE_INPUT2 = """R 5
U 8
L 8
D 3
R 17
D 10
L 25
U 20"""
EXAMPLE_SOLUTION_B2 = 36

DIRECTIONS = {'U': (-1, 0), 'L': (0, -1), 'D': (1, 0), 'R': (0, 1)}
re_motion = re.compile(r"(\w) (\d+)")


def parse_motion(line):
    m = re_motion.match(line)
    dir, steps = m.groups()
    return np.array(DIRECTIONS[dir]), int(steps)


def build_grid(path):
    arr2d = np.stack(path)
    r_min = arr2d[:, 0].min()
    r_max = arr2d[:, 0].max()
    c_min = arr2d[:, 1].min()
    c_max = arr2d[:, 1].max()
    grid = np.zeros((r_max - r_min + 1, c_max - c_min + 1)).astype('int32')
    offset = np.array((r_min, c_min))
    for step in path:
        loc = step - offset
        grid[loc[0], loc[1]] = 1
    return grid


def solve_a(puzzle_input, verbose=False):
    h = [np.array((0, 0), dtype='int32')]
    t = [np.array((0, 0), dtype='int32')]
    for line in puzzle_input.split('\n'):
        dir, steps = parse_motion(line)
        for i in range(steps):
            h.append(h[-1] + dir)
            delta = h[-1] - t[-1]
            vert_gap = (delta[0] == 0 and abs(delta[1]) > 1)
            horiz_gap = (delta[1] == 0 and abs(delta[0]) > 1)
            diag_gap = abs(delta[0]) + abs(delta[1]) > 2
            if vert_gap or horiz_gap or diag_gap:
                t.append(t[-1] + np.clip(delta, -1, 1))
    t_grid = build_grid(t)
    if verbose:
        print(t_grid)
    return t_grid.sum()


def solve_b(puzzle_input, verbose=False, n=10):
    seg = [[np.array((0, 0), dtype='int32')] for i in range(n)]
    for line in puzzle_input.split('\n'):
        dir, steps = parse_motion(line)
        for i in range(steps):
            seg[0].append(seg[0][-1] + dir)
            for j in range(1, n):
                delta = seg[j - 1][-1] - seg[j][-1]
                vert_gap = (delta[0] == 0 and abs(delta[1]) > 1)
                horiz_gap = (delta[1] == 0 and abs(delta[0]) > 1)
                diag_gap = abs(delta[0]) + abs(delta[1]) > 2
                if vert_gap or horiz_gap or diag_gap:
                    seg[j].append(seg[j][-1] + np.clip(delta, -1, 1))
    t_grid = build_grid(seg[-1])
    if verbose:
        print(t_grid)
    return t_grid.sum()


if __name__ == "__main__":
    puzzle_input = get_puzzle_input(__file__)

    assert solve_a(EXAMPLE_INPUT, verbose=True) == EXAMPLE_SOLUTION_A
    print(solve_a(puzzle_input))

    assert solve_b(EXAMPLE_INPUT, verbose=True) == EXAMPLE_SOLUTION_B
    assert solve_b(EXAMPLE_INPUT2, verbose=True) == EXAMPLE_SOLUTION_B2
    print(solve_b(puzzle_input))
