import pandas as pd
import numpy as np

LETTER_TO_POINTS = {'A': 1, 'B': 2, 'C': 3, 'X': 1, 'Y': 2, 'Z': 3}


def parse_input(fpath):
    with open(fpath) as f:
        raw_input = f.read().strip()
    return pd.DataFrame([round.split() for round in raw_input.split('\n')], columns=['opp', 'me'])


def solve_a(fpath):
    df = (
        parse_input(fpath)
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


def solve_b(fpath):
    df = (
        parse_input(fpath)
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
    assert solve_a('../data/p2a_ex.txt') == 15
    print(solve_a('../data/p2a.txt'))

    assert solve_b('../data/p2a_ex.txt') == 12
    print(solve_b('../data/p2a.txt'))
