from typing import List
from functools import reduce


def mostCommon(i: int, lines: List[str]) -> int:
    if reduce(lambda acc, x: acc + int(x[i]), lines, 0) >= len(lines) / 2:
        return 1
    return 0


def part1(nums: List[str]) -> int:
    gamma = {}
    epsilon = {}
    for i in range(len(nums[0])):
        gamma[i] = mostCommon(i, nums)
        epsilon[i] = (gamma[i] + 1) % 2
    gamma = int(''.join([str(v) for v in gamma.values()]), 2)
    epsilon = int(''.join([str(v) for v in epsilon.values()]), 2)
    return gamma * epsilon


def part2(nums: List[str]) -> int:
    o2 = nums.copy()
    co2 = nums.copy()
    for i in range(len(nums[0])):
        if len(o2) > 1:
            most_common = mostCommon(i, o2)
            o2 = list(filter(lambda x: int(x[i]) == most_common, o2))
        if len(co2) > 1:
            least_common = (mostCommon(i, co2) + 1) % 2
            co2 = list(filter(lambda x: int(x[i]) == least_common, co2))
    return int(o2[0], 2) * int(co2[0], 2)


if __name__ == "__main__":
    with open("input", 'r') as f:
        lines = list(map(lambda x: x.strip(), f.readlines()))
    print(f"part1: {part1(lines)}")
    print(f"part2: {part2(lines)}")
