# Encoding Error
# https://adventofcode.com/2020/day/9

from typing import List
from collections import deque

def part_one(data: List[int]) -> int:
    """Returns the first element in `data` which does not have a pair of numbers
    among the previous 25 elements before it that add up to it.
    """
    options = deque(data[:25], maxlen=25)

    for i in range(25, len(data)):
        candidate = data[i]

        if not has_two_sum(list(options), candidate):
            return candidate

        options.append(candidate)

    return


def has_two_sum(data: List[int], total: int) -> bool:
    """Returns True if `data` contains a pair of numbers that add to `total`,
    else, returns False.
    """
    seen = dict()

    for num in sorted(data):
        target = total - num

        if target in seen:
            return True

        seen[num] = num

    return False


def part_two(data):
    pass


if __name__ == "__main__":
    with open("data.txt") as f:
        data = f.readlines()
        data = list(map(int, data))

    print("Part one:", part_one(data))
    print("Part two:", part_two(data))
