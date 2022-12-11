import re
from functools import reduce
from tqdm import tqdm
import pandas as pd
import numpy as np
from utils import get_puzzle_input

EXAMPLE_INPUT = """Monkey 0:
  Starting items: 79, 98
  Operation: new = old * 19
  Test: divisible by 23
    If true: throw to monkey 2
    If false: throw to monkey 3

Monkey 1:
  Starting items: 54, 65, 75, 74
  Operation: new = old + 6
  Test: divisible by 19
    If true: throw to monkey 2
    If false: throw to monkey 0

Monkey 2:
  Starting items: 79, 60, 97
  Operation: new = old * old
  Test: divisible by 13
    If true: throw to monkey 1
    If false: throw to monkey 3

Monkey 3:
  Starting items: 74
  Operation: new = old + 3
  Test: divisible by 17
    If true: throw to monkey 0
    If false: throw to monkey 1"""
EXAMPLE_SOLUTION_A = 10605
EXAMPLE_SOLUTION_B = 2713310158

re_monkey = re.compile(
    (
        r"Monkey (?P<id>\d+):\s+"
        r"Starting items: (?P<items>[^\n]+)\s+"
        r"Operation: new = (?P<op>[^\n]+)\s+"
        r"Test: divisible by (?P<div_by>\d+)\s+"
        r"If true: throw to monkey (?P<if_true>\d+)\s+"
        r"If false: throw to monkey (?P<if_false>\d+)"
    ),
    re.MULTILINE,
)


def build_op(op_str):
    return lambda old: eval(op_str, None, {"old": old})


def parse_monkeys(puzzle_input):
    monkeys = []
    for i, match in enumerate(re_monkey.finditer(puzzle_input)):
        monkey_dict = match.groupdict()
        assert i == int(monkey_dict['id'])
        del monkey_dict['id']
        monkey_dict['items'] = [int(item) for item in monkey_dict['items'].split(', ')]
        monkey_dict['op'] = build_op(monkey_dict['op'])
        for key in ['div_by', 'if_true', 'if_false']:
            monkey_dict[key] = int(monkey_dict[key])
        monkey_dict['inspected'] = 0
        monkeys.append(monkey_dict)
    return monkeys


def get_inspected(monkeys):
    return [monkey['inspected'] for monkey in monkeys]


def solve_a(puzzle_input):
    monkeys = parse_monkeys(puzzle_input)
    for i in range(1, 21):
        for monkey_id, monkey in enumerate(monkeys):
            # print(f"Round {i}, monkey {monkey_id}: {monkey}")
            while monkey['items']:
                monkey['inspected'] += 1
                item = monkey['items'].pop(0)
                item = monkey['op'](item)
                item //= 3
                throw_to = monkey['if_true'] if item % monkey['div_by'] == 0 else monkey['if_false']
                # print(f"  Throw item with worry value {item} to monkey {throw_to}.")
                monkeys[throw_to]['items'].append(item)
    inspected = sorted(get_inspected(monkeys))
    return inspected[-1] * inspected[-2]


def solve_b(puzzle_input):
    monkeys = parse_monkeys(puzzle_input)

    # all monkeys test using modulo, so we only need to store a remainder for each item.
    # however, we don't know which monkey(s) might get an item in the future,
    # so the safest thing is to calculate the remainder using
    # the product of all monkeys' divisors (all_divs) as the modulus.
    all_divs = reduce(lambda a, b: a * b, [monkey["div_by"] for monkey in monkeys])

    for i in tqdm(range(1, 10001)):
        for monkey_id, monkey in enumerate(monkeys):
            while monkey['items']:
                monkey['inspected'] += 1
                item = monkey['items'].pop(0)
                item = monkey['op'](item)
                item %= all_divs  # this is where we only store a remainder for each item
                throw_to = monkey['if_true'] if item % monkey['div_by'] == 0 else monkey['if_false']
                monkeys[throw_to]['items'].append(item)
    inspected = sorted(get_inspected(monkeys))
    return inspected[-1] * inspected[-2]


if __name__ == "__main__":
    puzzle_input = get_puzzle_input(__file__)

    assert solve_a(EXAMPLE_INPUT) == EXAMPLE_SOLUTION_A
    print(solve_a(puzzle_input))

    assert solve_b(EXAMPLE_INPUT) == EXAMPLE_SOLUTION_B
    print(solve_b(puzzle_input))
