from typing import List, Tuple

inst_lookup = {
    "forward": ('x', 1),
    "down": ('z', 1),
    "up": ('z', -1)
}


def part1(directions: List[Tuple[str, int]]) -> int:
    pos = {
        'x': 0,
        'z': 0
    }
    for inst in directions:
        lookup_res = inst_lookup[inst[0]]
        pos[lookup_res[0]] += inst[1] * lookup_res[1]
    return pos['x'] * pos['z']


def part2(nums: List[int]) -> int:
    pos = {
        'x': 0,
        'z': 0,
        'a': 0
    }
    for inst in directions:
        if inst[0] == "forward":
            pos['x'] += inst[1]
            pos['z'] += inst[1] * pos['a']
        else:
            lookup_res = inst_lookup[inst[0]]
            pos['a'] += inst[1] * lookup_res[1]
    return pos['x'] * pos['z']


if __name__ == "__main__":
    with open("input", 'r') as f:
        lines = f.readlines()
    directions = list(map(lambda x: x.split(), lines))
    directions = list(map(lambda x: (x[0], int(x[1])), directions))
    print(f"part1: {part1(directions)}")
    print(f"part2: {part2(directions)}")
