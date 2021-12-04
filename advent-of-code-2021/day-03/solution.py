# Binary Diagnostic
# https://adventofcode.com/2021/day/3

from typing import List
from collections import defaultdict


def part_one(data: List[List[int]]) -> int:
    """Map place values to the total sum of numbers under each place value. 
    Use the sum to determine if the place value's final number should be 0 or 1.
    """
    COLUMNS = len(data[0])  # place values
    ROWS = len(data)  # digits
    place_value_dict = defaultdict(int) # k-> place value, v-> sum of nums under value
    gamma, epsilon = "", ""

    # Map place values.
    for col in range(COLUMNS):
        for row in range(ROWS):
            place_value_dict[col] += data[row][col]

    # Build gamma and epsilon binary strings.
    for col in range(COLUMNS):
        # Check if at least 50% of nums in current column are ones.
        value = place_value_dict[col] / ROWS >= 0.5  # bool

        # Set gamma and epsilon.
        gamma += str(int(value))
        epsilon += str(int(not value))

    return int(gamma, 2) * int(epsilon, 2)


def part_two(data):
    pass


if __name__ == '__main__':
    with open("data.txt") as f:
        # convert input to a matrix of ints
        data = map(
            lambda x: list(map(int, list(x.strip()))),
            f.readlines())
        data = list(data)  # make subscriptable

    print("Part one:", part_one(data))
    print("Part two:", part_two(data))
