import json
import re
from functools import reduce
import pandas as pd
import numpy as np
from utils import get_puzzle_input

EXAMPLE_INPUT = """$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k"""
EXAMPLE_SOLUTION_A = 95437
EXAMPLE_SOLUTION_B = 24933642

re_dir = re.compile(r"dir (\S+)")
re_file = re.compile(r"(\d+) (\S+)")
re_cd = re.compile(r"\$ cd (\S+)")


def parse_dir_structure(puzzle_input):
    lines = puzzle_input.split('\n')
    root = {}
    cwd = None
    is_ls = False
    for line in lines:
        if is_ls:
            if line.startswith("$"):
                is_ls = False
            else:
                parent = reduce(lambda a, b: a[b], cwd)
                if newdir := re_dir.match(line):
                    if newdir.group(1) in parent.keys():
                        raise Exception(f"dir `{newdir.group(1)}` already exists at `{cwd}`.")
                    parent[newdir.group(1)] = {}
                else:
                    newfile = re_file.match(line)
                    parent[newfile.group(2)] = int(newfile.group(1))
        if line == "$ cd /":
            cwd = [root]
        elif line == "$ ls":
            is_ls = True
        elif cddir := re_cd.match(line):
            newdir = cddir.group(1)
            if newdir == "..":
                cwd.pop()
            else:
                cwd.append(newdir)
    return root


def dir_size(dir):
    size = 0
    all_child_sizes = []
    for k, v in dir.items():
        if isinstance(v, dict):
            child_sizes = dir_size(v)
            all_child_sizes += child_sizes
            size += child_sizes[0]
        else:
            size += v
    return [size] + all_child_sizes


def solve_a(puzzle_input, verbose=False):
    root = parse_dir_structure(puzzle_input)
    if verbose:
        print(json.dumps(root, indent=2))
    all_sizes = dir_size(root)
    return sum(v for v in all_sizes if v <= 100_000)


def solve_b(puzzle_input):
    root = parse_dir_structure(puzzle_input)
    all_sizes = dir_size(root)
    space_required = 30_000_000 - (70_000_000 - all_sizes[0])
    return min(x for x in all_sizes if x >= space_required)


if __name__ == "__main__":
    puzzle_input = get_puzzle_input(__file__)

    assert solve_a(EXAMPLE_INPUT, verbose=True) == EXAMPLE_SOLUTION_A
    print(solve_a(puzzle_input))

    assert solve_b(EXAMPLE_INPUT) == EXAMPLE_SOLUTION_B
    print(solve_b(puzzle_input))
