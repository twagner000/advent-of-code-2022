import pandas as pd
import numpy as np
from utils import get_puzzle_input

EXAMPLE_INPUT = """addx 15
addx -11
addx 6
addx -3
addx 5
addx -1
addx -8
addx 13
addx 4
noop
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx -35
addx 1
addx 24
addx -19
addx 1
addx 16
addx -11
noop
noop
addx 21
addx -15
noop
noop
addx -3
addx 9
addx 1
addx -3
addx 8
addx 1
addx 5
noop
noop
noop
noop
noop
addx -36
noop
addx 1
addx 7
noop
noop
noop
addx 2
addx 6
noop
noop
noop
noop
noop
addx 1
noop
noop
addx 7
addx 1
noop
addx -13
addx 13
addx 7
noop
addx 1
addx -33
noop
noop
noop
addx 2
noop
noop
noop
addx 8
noop
addx -1
addx 2
addx 1
noop
addx 17
addx -9
addx 1
addx 1
addx -3
addx 11
noop
noop
addx 1
noop
addx 1
noop
noop
addx -13
addx -19
addx 1
addx 3
addx 26
addx -30
addx 12
addx -1
addx 3
addx 1
noop
noop
noop
addx -9
addx 18
addx 1
addx 2
noop
noop
addx 9
noop
noop
noop
addx -1
addx 2
addx -37
addx 1
addx 3
noop
addx 15
addx -21
addx 22
addx -6
addx 1
noop
addx 2
addx 1
noop
addx -10
noop
noop
addx 20
addx 1
addx 2
addx 2
addx -6
addx -11
noop
noop
noop"""
EXAMPLE_SOLUTION_A = 13140
EXAMPLE_SOLUTION_B = """##..##..##..##..##..##..##..##..##..##..
###...###...###...###...###...###...###.
####....####....####....####....####....
#####.....#####.....#####.....#####.....
######......######......######......####
#######.......#######.......#######....."""

TARGET_CYCLES = (20, 60, 100, 140, 180, 220)


def solve_a(puzzle_input):
    x = 1
    prog = puzzle_input.split('\n')
    target_signals = []
    inst = None
    for_cycle = None
    for cycle in range(1, 221):
        if cycle == for_cycle:
            x += int(inst.split()[-1])
            inst = None
        if inst is None:
            inst = prog.pop(0)
            if inst.startswith("addx"):
                for_cycle = cycle + 2
            else:
                inst = None
        if cycle in TARGET_CYCLES:
            target_signals.append(cycle * x)
    return sum(target_signals)


def get_char(cycle, x):
    if abs(x - ((cycle - 1) % 40)) <= 1:
        return "#"
    return "."


def solve_b(puzzle_input):
    x = 1
    prog = puzzle_input.split('\n')
    inst = None
    for_cycle = None
    rows = ["" for i in range(6)]
    for cycle in range(1, 241):
        if cycle == for_cycle:
            x += int(inst.split()[-1])
            inst = None
        if inst is None:
            inst = prog.pop(0)
            if inst.startswith("addx"):
                for_cycle = cycle + 2
            else:
                inst = None
        rows[(cycle - 1) // 40] += get_char(cycle, x)
    return '\n'.join(rows)


if __name__ == "__main__":
    puzzle_input = get_puzzle_input(__file__)

    assert solve_a(EXAMPLE_INPUT) == EXAMPLE_SOLUTION_A
    print(solve_a(puzzle_input))

    assert solve_b(EXAMPLE_INPUT) == EXAMPLE_SOLUTION_B
    print(solve_b(puzzle_input))
