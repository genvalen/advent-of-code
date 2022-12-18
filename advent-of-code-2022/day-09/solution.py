# Day 8: Treetop Tree House
# https://adventofcode.com/2022/day/8

from typing import List


def part_one(map_: List[str]) -> int:
    pass


def part_two(data: List[str]) -> int:
    pass


if __name__ == "__main__":
    with open("data.txt") as f:
        data = f.readlines()

    with open("output.txt", "a") as f:
        f.write("Part one: " + str(part_one(data)) + "\n")
        f.write("Part two: " + str(part_two(data)) + "\n")

    print("Part one:", part_one(data))
    print("Part two:", part_two(data))
