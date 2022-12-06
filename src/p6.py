import pandas as pd
import numpy as np
from utils import get_puzzle_input

EXAMPLES = [
    ("mjqjpqmgbljsphdztnvjfqwrcgsmlb", 7, 19),
    ("bvwbjplbgvbhsrlpgdmjqwftvncz", 5, 23),
    ("nppdvjthqldpwncqszvftbrmjlhg", 6, 23),
    ("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", 10, 29),
    ("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw", 11, 26),
]
EXAMPLE_SOLUTION_B = None


def detect_first_substr_with_unique_letters(str_, substr_len):
    for i in range(len(str_) - substr_len + 1):
        if len(set(str_[i:i + substr_len])) == substr_len:
            return i + substr_len


def solve_a(puzzle_input):
    return detect_first_substr_with_unique_letters(puzzle_input, 4)


def solve_b(puzzle_input):
    return detect_first_substr_with_unique_letters(puzzle_input, 14)


if __name__ == "__main__":
    puzzle_input = get_puzzle_input(__file__)

    for example in EXAMPLES:
        assert solve_a(example[0]) == example[1]
    print(solve_a(puzzle_input))

    for example in EXAMPLES:
        assert solve_b(example[0]) == example[2]
    print(solve_b(puzzle_input))
