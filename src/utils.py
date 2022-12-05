from pathlib import Path


def get_puzzle_input(script_path):
    p = Path(script_path)
    with open(p.parent.parent / 'data' / p.parts[-1].replace('.py', '.txt'), 'r') as f:
        return f.read().strip()
