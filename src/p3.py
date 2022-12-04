import pandas as pd
from functools import reduce

PRIORITY = " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"


def parse_input(fpath):
    with open(fpath) as f:
        lines = f.readlines()
    return lines


def reduce_intersect(row):
    return list(reduce(lambda a, b: a.intersection(b), row))[0]


def solve_a(fpath):
    df = (
        pd.DataFrame({'raw': parse_input(fpath)})
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


def solve_b(fpath):
    df = (
        pd.DataFrame({'raw': parse_input(fpath)})
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
    assert solve_a('../data/p3a_ex.txt') == 157
    print(solve_a('../data/p3a.txt'))

    assert solve_b('../data/p3a_ex.txt') == 70
    print(solve_b('../data/p3a.txt'))
