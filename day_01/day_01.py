from typing import List


def inc_count(nums: List[int]) -> int:
    """
    Returns how many times nums[i] > nums[i-1].
    Ignores the first value as there is nothing to compare to.
    """
    inc_count = 0
    for i in range(1, len(nums)):
        inc_count += nums[i] > nums[i-1]
    return inc_count


def part1(nums: List[int]) -> int:
    return inc_count(nums)


def part2(nums: List[int]) -> int:
    moving_avg = []
    for i in range(3, len(nums)+1):
        moving_avg.append(sum(nums[i-3:i]))
    return inc_count(moving_avg)


if __name__ == "__main__":
    with open("input", 'r') as f:
        numbers = list(map(int, f.readlines()))
    print(f"part1: {part1(numbers)}")
    print(f"part2: {part2(numbers)}")
