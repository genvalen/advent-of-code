# Day 4: Camp Cleanup
# https://adventofcode.com/2022/day/4

from typing import List


def part_one(data: List[str]) -> int:
    total = 0

    for line in data:
        p1, p2 = line.split(",")
        start1, end1 = map(int, p1.split("-"))
        start2, end2 = map(int, p2.split("-"))

        if start1 <= start2 and end2 <= end1:  # first pair fully immerses second
            total += 1

        elif start2 <= start1 and end1 <= end2:  # second pair fully immerses first
            total += 1

    return total


def part_two(data: List[str]) -> int:
    total = 0

    for line in data:
        p1, p2 = line.split(",")
        start1, end1 = map(int, p1.split("-"))
        start2, end2 = map(int, p2.split("-"))

        if start2 <= end1 <= end2:  # end1 overlaps second interval pair
            total += 1

        elif start1 <= end2 <= end1:  # end2 overlaps first interval pair
            total += 1

    return total


if __name__ == "__main__":
    with open("data.txt") as f:
        data = f.readlines()

    with open("output.txt", "a") as f:
        f.write("Part one: " + str(part_one(data)) + "\n")
        f.write("Part two: " + str(part_two(data)) + "\n")

    print("Part one:", part_one(data))
    print("Part two:", part_two(data))
