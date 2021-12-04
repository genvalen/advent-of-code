# Dive!
# https://adventofcode.com/2021/day/2

from typing import List


def part_one(data: List[str]) -> int:
    """Update x and y coordinates according to instructions
    in the input list.
    """
    x, y = 0, 0

    for instruction in data:
        code, value = instruction.split()
        value = int(value)

        if code == "forward":
            x += value
        elif code == "down":
            y += value
        elif code == "up":
            y -= value

    return x * y


def part_two(data: List[str]) -> int:
    """Update x, y and z coordinates according to instructions
    in the input list.
    """
    x, y, z = 0, 0, 0

    for instruction in data:
        code, value = instruction.split()
        value = int(value)

        if code == "forward":
            x += value
            y += value * z
        elif code == "down":
            z += value
        elif code == "up":
            z -= value

    return x * y


if __name__ == '__main__':
    with open("data.txt") as f:
        data = f.readlines()

    print("Part one:", part_one(data))
    print("Part two:", part_two(data))
