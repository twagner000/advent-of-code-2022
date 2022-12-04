
def get_calories(fname):
    with open(fname, 'r') as f:
        raw_input = f.read().strip()
    elf_sums = [
        sum(int(food) for food in elf.split('\n'))
        for elf in raw_input.split('\n\n')
    ]
    return elf_sums


def solve_a(fname):
    return max(get_calories(fname))


def solve_b(fname):
    return sum(sorted(get_calories(fname))[-3:])


if __name__ == "__main__":
    assert solve_a('../data/p1a_ex.txt') == 24_000
    print(solve_a('../data/p1a.txt'))

    assert solve_b('../data/p1a_ex.txt') == 45_000
    print(solve_b('../data/p1a.txt'))
