# Adapter Array
# https://adventofcode.com/2020/day/10

from typing import List

def part_one(data: List[int]) -> int:
    """Arrange a list of adapters (ints) so that adjacent adapters have
    a difference of, at most, 3.

    Return the number of times adapters have a difference of 1 multiplied by
    the number of times they have a difference of 3.
    """
    from collections import defaultdict

    d = defaultdict(int)
    MAX = 3
    prev = 0

    data.sort()

    # calculate diff between adjacent adapters
    for cur in data:
        diff = cur - prev
        if diff <= MAX:
            d[diff] += 1
        prev = cur

    # account for the built-in adapter
    d[MAX] += 1

    return d[1] * d[3]


def part_two(data):
    pass


if __name__ == "__main__":
    with open("data.txt") as f:
        data = f.readlines()
        data = list(map(int, data))

    print("Part one:", part_one(data))
    print("Part two:", part_two(data))
