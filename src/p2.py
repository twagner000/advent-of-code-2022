import pandas as pd
import numpy as np
from utils import get_puzzle_input

EXAMPLE_INPUT = """A Y
B X
C Z"""
EXAMPLE_SOLUTION_A = 15
EXAMPLE_SOLUTION_B = 12

LETTER_TO_POINTS = {'A': 1, 'B': 2, 'C': 3, 'X': 1, 'Y': 2, 'Z': 3}


def parse_input(puzzle_input):
    return pd.DataFrame([round.split() for round in puzzle_input.split('\n')], columns=['opp', 'me'])


def solve_a(puzzle_input):
    df = (
        parse_input(puzzle_input)
        .applymap(LETTER_TO_POINTS.get)
        .assign(
            my_win=lambda df: np.select([
                df['me'] == df['opp'],
                df['me'] == df['opp'] + 1,
                (df['me'] == 1) & (df['opp'] == 3),
            ], [3, 6, 6], 0),
            my_points=lambda df: df['me'] + df['my_win'],
        )
    )
    return df['my_points'].sum()


def solve_b(puzzle_input):
    df = (
        parse_input(puzzle_input)
        .applymap(LETTER_TO_POINTS.get)
        .assign(
            my_win=lambda df: (df['me'] - 1) * 3,
            me=lambda df: np.select([
                df['my_win'] == 0,
                df['my_win'] == 6,
            ], [
                (df['opp'] - 2) % 3 + 1,
                df['opp'] % 3 + 1,
            ], df['opp']),
            my_points=lambda df: df['me'] + df['my_win'],
        )
    )
    return df['my_points'].sum()


if __name__ == "__main__":
    puzzle_input = get_puzzle_input(__file__)

    assert solve_a(EXAMPLE_INPUT) == EXAMPLE_SOLUTION_A
    print(solve_a(puzzle_input))

    assert solve_b(EXAMPLE_INPUT) == EXAMPLE_SOLUTION_B
    print(solve_b(puzzle_input))
