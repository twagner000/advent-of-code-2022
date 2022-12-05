import pandas as pd
import numpy as np
from utils import get_puzzle_input

EXAMPLE_INPUT = """TBD"""
EXAMPLE_SOLUTION_A = -1
EXAMPLE_SOLUTION_B = None


def solve_a(puzzle_input):
    return (
        pd.DataFrame({'raw': puzzle_input.split('\n')})
    )


def solve_b(puzzle_input):
    return (
        pd.DataFrame({'raw': puzzle_input.split('\n')})
    )


if __name__ == "__main__":
    puzzle_input = get_puzzle_input(__file__)

    assert solve_a(EXAMPLE_INPUT) == EXAMPLE_SOLUTION_A
    print(solve_a(puzzle_input))

    assert solve_b(EXAMPLE_INPUT) == EXAMPLE_SOLUTION_B
    print(solve_b(puzzle_input))
