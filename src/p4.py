import pandas as pd
from utils import get_puzzle_input

EXAMPLE_INPUT = """2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8"""
EXAMPLE_SOLUTION_A = 2
EXAMPLE_SOLUTION_B = 4


def prep_sets(puzzle_input):
    return (
        pd.DataFrame({'raw': puzzle_input.split('\n')})
        ['raw'].str.split('[-,]', expand=True).astype(int)
        .rename(columns=lambda x: f"e{x // 2 + 1}_{x % 2}")
        .assign(
            e1=lambda df: df.apply(lambda x: set(range(x['e1_0'], x['e1_1'] + 1)), axis=1),
            e2=lambda df: df.apply(lambda x: set(range(x['e2_0'], x['e2_1'] + 1)), axis=1),
        )
    )


def solve_a(puzzle_input):
    return (
        prep_sets(puzzle_input)
        .assign(
            contained=lambda df: 1 * df.apply(lambda x: x['e1'].issubset(x['e2']) or x['e2'].issubset(x['e1']), axis=1),
        )
        ['contained'].sum()
    )


def solve_b(puzzle_input):
    return (
        prep_sets(puzzle_input)
        .assign(
            overlap=lambda df: df.apply(lambda x: len(x['e1'].intersection(x['e2'])), axis=1).clip(upper=1),
        )
        ['overlap'].sum()
    )


if __name__ == "__main__":
    puzzle_input = get_puzzle_input(__file__)

    assert solve_a(EXAMPLE_INPUT) == EXAMPLE_SOLUTION_A
    print(solve_a(puzzle_input))

    assert solve_b(EXAMPLE_INPUT) == EXAMPLE_SOLUTION_B
    print(solve_b(puzzle_input))
