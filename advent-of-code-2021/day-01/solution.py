# Sonar Sweep
# https://adventofcode.com/2021/day/1

from typing import List


def part_one(data: List[int]) -> int:
    """Return number of times an int in a stream of input
    is greater than the previous int.
    """
    count = 0
    prev_num = 0

    for num in data:
        if num > prev_num:
            count += 1
        prev_num = num

    return count - 1  # subtract initial comparison (against 0)


def part_two(data: List[int]) -> int:
    """Using a sliding window of size three, return the number of times
    the sum of a triplet is greater than the sum of the previous triplet.
    """
    count = 0
    prev_triplet = sum(data[0:3])  # sum of initial triplet
    prev_leading_num = data[0]  # leading number of the initial triplet

    for index, cur_num in enumerate(data[3:], 3):
        triplet = prev_triplet - prev_leading_num + cur_num

        if triplet > prev_triplet:
            count += 1

        prev_triplet = triplet
        prev_leading_num = data[index - 2]

    return count


if __name__ == "__main__":
    with open("data.txt") as f:
        data = list(map(int, f.readlines()))

    print("Part one:", part_one(data))
    print("Part two:", part_two(data))
