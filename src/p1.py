from utils import get_puzzle_input

EXAMPLE_INPUT = """1000
2000
3000

4000

5000
6000

7000
8000
9000

10000"""
EXAMPLE_SOLUTION_A = 24_000
EXAMPLE_SOLUTION_B = 45_000


def get_calories(puzzle_input):
    elf_sums = [
        sum(int(food) for food in elf.split('\n'))
        for elf in puzzle_input.split('\n\n')
    ]
    return elf_sums


def solve_a(puzzle_input):
    return max(get_calories(puzzle_input))


def solve_b(puzzle_input):
    return sum(sorted(get_calories(puzzle_input))[-3:])


if __name__ == "__main__":
    puzzle_input = get_puzzle_input(__file__)

    assert solve_a(EXAMPLE_INPUT) == EXAMPLE_SOLUTION_A
    print(solve_a(puzzle_input))

    assert solve_b(EXAMPLE_INPUT) == EXAMPLE_SOLUTION_B
    print(solve_b(puzzle_input))
