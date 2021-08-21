# Binary Boarding
# https://adventofcode.com/2020/day/5

from typing import List

def part_one(data: List[str]) -> int:
    """Return passenger ID with the highest numerical value."""
    max_id = 0

    for line in data:
        cur_id = get_seat_ID(line)
        max_id = max(max_id, cur_id)

    return max_id


def part_two(data: List[str]) -> int:
    """Identify missing ID and return its value."""
    max_id = part_one(data)
    min_id = max_id
    ids_seen = set()

    for line in data:
        cur_id = get_seat_ID(line)
        ids_seen.add(cur_id)
        min_id = min(min_id, cur_id)

    missing_id = set(range(min_id, max_id+1)).difference(ids_seen).pop()

    return missing_id


def get_seat_ID(directions: str) -> int:
    """Generate an ID based on passenger seating information."""
    # get directions for row and col
    row_directions = directions[:7]
    col_directions = directions[7:]

    # identify correct row, col, and seat ID
    row = binary_parser(0, 127, row_directions)
    col = binary_parser(0, 7, col_directions)
    id_ = row*8 + col

    return id_


def binary_parser(start: int, end: int, directions: str) -> int:
    """Apply binary search to traverse a range determined by input.

    Traversal instructions:
    For each char in `directions` that is visited (starting with midpoint),
    shorten the range by moving into the half determiend by said char:
    F/L -> left, B/R -> right.
    """
    left, right = start, end
    pointer = 0
    mid = 0

    while pointer < len(directions):
        mid = left + (right-left) // 2

        # move into lower half
        if directions[pointer] in "FL":
            right = mid

        # move into upper half
        elif directions[pointer] in "BR":
            left = mid + 1

        pointer += 1

    return left


if __name__ == "__main__":
    with open("data.txt") as f:
        data = f.readlines()

    print("Part one:", part_one(data))
    print("Part two:", part_two(data))
