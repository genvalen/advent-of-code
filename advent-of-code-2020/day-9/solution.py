# Encoding Error
# https://adventofcode.com/2020/day/9

from typing import List
from collections import deque

def part_one(data: List[int]) -> int:
    """Returns the first element in `data` which does not have a pair of numbers
    among the previous 25 elements before it that add up to itself.
    """
    options = deque(data[:25], maxlen=25)

    for i in range(25, len(data)):
        candidate = data[i]

        if not has_two_sum(list(options), candidate):
            return candidate

        options.append(candidate)

    return -1


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


def part_two(data: List[int]) -> int:
    """Find a contiguous set of numbers that add up to a target and return
    the sum of the smallest and largest number in the set."""
    target = part_one(data)
    length = len(data)
    ptr1, ptr2 = 0, 1

    while ptr2 < length:
        cur_sum = sum(data[ptr1:ptr2+1])

        if cur_sum == target:
            sublist = data[ptr1:ptr2+1]
            return min(sublist) + max(sublist)

        # increase sublist
        ptr2 += 1

        # decrease sublist from the left, if needed
        if cur_sum > target:
            while cur_sum > target and ptr2 < length:
                ptr1 += 1

                # Ensure sublist maintains a min of two elements
                if ptr2 - ptr1 == 0:
                    ptr2 += 1

                cur_sum = sum(data[ptr1:ptr2+1])
    
    return -1


if __name__ == "__main__":
    with open("data.txt") as f:
        data = f.readlines()
        data = list(map(int, data))

    print("Part one:", part_one(data))
    print("Part two:", part_two(data))
