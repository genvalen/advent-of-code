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


def part_two(data: List[List[int]]) -> int:
    oxygen, co2 = data.copy(), data.copy()
    data_subset = defaultdict(list)

    # Find oxygen value.
    col = 0
    while len(oxygen) > 1:
        for row in range(len(oxygen)):
            cur = oxygen[row][col]
            if cur == 1:
                data_subset[1].append(oxygen[row])
            else:
                data_subset[0].append(oxygen[row])


            # Select a subset to move forward with based on condition.
            if row == len(oxygen) - 1:
                max_ = 1 if (len(data_subset[1]) / len(oxygen)) >= 0.5 else 0
                oxygen = data_subset[max_].copy()
                data_subset.clear()
        col += 1

    # Find co2 value.
    col = 0
    while len(co2) > 1:
        for row in range(len(co2)):
            cur = co2[row][col]
            if cur == 1:
                data_subset[1].append(co2[row])
            else:
                data_subset[0].append(co2[row])

            # Select a subset to move forward with based on condition.
            if row == len(co2) - 1:
                min_ = 0 if (len(data_subset[0]) / len(co2)) <= 0.5 else 1
                co2 = data_subset[min_].copy()
                data_subset.clear()
        col += 1

    # Build oxygen and co2 binary strings.
    oxygen = "".join(map(str, oxygen[0]))
    co2 = "".join(map(str, co2[0]))

    return int(oxygen, 2) * int(co2, 2)


if __name__ == '__main__':
    with open("data.txt") as f:
        # convert input to a matrix of ints
        data = map(
            lambda x: list(map(int, list(x.strip()))),
            f.readlines())
        data = list(data)  # make subscriptable

    print("Part one:", part_one(data))
    print("Part two:", part_two(data))
