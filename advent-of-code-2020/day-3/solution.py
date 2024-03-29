# Toboggan Trajectory
# https://adventofcode.com/2020/day/3

from typing import List, Tuple, Set

def part_one(map: List[str], right: int = 3, down: int = 1) -> int:
    """Return number of times coordinate lands on "#" symbol while
    traversing map."""
    row_len, col_len = len(map), len(map[0])
    row, col = 0, 0 #starting coordinate
    count = 0

    while row < row_len:
        if map[row][col] == "#":
            count += 1

        # update coordinate
        row += down
        col = (col + right) % col_len #wrap cols

    return count


def part_two(map: List[str], slopes: Set[Tuple[int, int]]) -> int:
    """Return the product of the results of traveling down the map
    according to each slope provided."""
    product = 1
    for right, down in slopes:
        result = part_one(map, right, down)
        product *= result

    return product


if __name__ == "__main__":
    with open("data.txt") as f:
        data = [line.strip() for line in f]

    slopes = {(1,1), (3,1), (5,1), (7,1), (1,2)}

    print("Part one:", part_one(data))
    print("Part two:", part_two(data, slopes))
