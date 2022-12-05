import re
import pandas as pd
import numpy as np
from utils import get_puzzle_input

EXAMPLE_INPUT = """    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2"""
EXAMPLE_SOLUTION_A = "CMZ"
EXAMPLE_SOLUTION_B = "MCD"

re_inst = re.compile(r'move (\d+) from (\d+) to (\d+)')


def parse_instruction(inst):
    try:
        return tuple(int(x) for x in re_inst.match(inst).groups())
    except AttributeError:
        return 0, None, None


def parse_input(puzzle_input):
    lines = puzzle_input.split('\n')
    for line_num, line_text in enumerate(lines):
        if line_text.startswith('move'):
            break

    init_stacks_str = lines[:line_num - 2][::-1]
    init_stacks = [row[1::4] for row in init_stacks_str]
    stacks = [[row[col] for row in init_stacks if row[col] != ' '] for col in range(len(init_stacks[0]))]

    return stacks, lines[line_num:]


def solve_a(puzzle_input):
    stacks, insts = parse_input(puzzle_input)
    for inst in insts:
        how_many, from_stack, to_stack = parse_instruction(inst)
        for i in range(how_many):
            stacks[to_stack - 1].append(stacks[from_stack - 1].pop())
    return ''.join(stack[-1] for stack in stacks)


def solve_b(puzzle_input):
    stacks, insts = parse_input(puzzle_input)
    for inst in insts:
        how_many, from_stack, to_stack = parse_instruction(inst)
        if how_many:
            stacks[to_stack - 1] += stacks[from_stack - 1][-how_many:]
            stacks[from_stack - 1] = stacks[from_stack - 1][:-how_many]
    return ''.join(stack[-1] for stack in stacks)


if __name__ == "__main__":
    puzzle_input = get_puzzle_input(__file__, strip=False)

    assert solve_a(EXAMPLE_INPUT) == EXAMPLE_SOLUTION_A
    print(solve_a(puzzle_input))

    assert solve_b(EXAMPLE_INPUT) == EXAMPLE_SOLUTION_B
    print(solve_b(puzzle_input))
