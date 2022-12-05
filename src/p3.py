import pandas as pd
from functools import reduce
from utils import get_puzzle_input

EXAMPLE_INPUT = """vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw"""
EXAMPLE_SOLUTION_A = 157
EXAMPLE_SOLUTION_B = 70

PRIORITY = " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"


def reduce_intersect(row):
    return list(reduce(lambda a, b: a.intersection(b), row))[0]


def solve_a(puzzle_input):
    df = (
        pd.DataFrame({'raw': puzzle_input.split('\n')})
        .assign(
            raw=lambda df: df['raw'].str.strip(),
            len=lambda df: df['raw'].str.len(),
            comp1=lambda df: df.apply(lambda x: x['raw'][:x['len'] // 2], axis=1),
            comp2=lambda df: df.apply(lambda x: x['raw'][x['len'] // 2:], axis=1),
            common=lambda df: df[['comp1', 'comp2']].applymap(set).apply(reduce_intersect, axis=1),
            priority=lambda df: df['common'].apply(PRIORITY.index),
        )
    )
    return df['priority'].sum()


def solve_b(puzzle_input):
    df = (
        pd.DataFrame({'raw': puzzle_input.split('\n')})
        .assign(
            raw=lambda df: df['raw'].str.strip(),
            group=lambda df: df.index // 3,
            elf=lambda df: df.index % 3,
        )
        .pivot_table('raw', 'group', 'elf', aggfunc='first')
        .assign(
            common=lambda df: df.applymap(set).apply(reduce_intersect, axis=1),
            priority=lambda df: df['common'].apply(PRIORITY.index),
        )
    )
    return df['priority'].sum()


if __name__ == "__main__":
    puzzle_input = get_puzzle_input(__file__)

    assert solve_a(EXAMPLE_INPUT) == EXAMPLE_SOLUTION_A
    print(solve_a(puzzle_input))

    assert solve_b(EXAMPLE_INPUT) == EXAMPLE_SOLUTION_B
    print(solve_b(puzzle_input))
