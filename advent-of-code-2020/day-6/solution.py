# Custom Customs
# https://adventofcode.com/2020/day/6

from typing import Set

def part_one(data: list) -> int:
    count = 0
    responses: Set[int] = set()

    eof_marker = ["\n"]

    for line in data + eof_marker:
        if line == "\n":
            count += len(responses)
            responses.clear()

        line = line.strip("\n")
        responses.update(list(line))

    return count


def part_two(data: list) -> int:
    count = 0
    responses: Set[int] = set()
    eof_marker = ["\n"]
    is_new_group = True

    for line in data + eof_marker:
        if line == "\n":
            count += len(responses)
            responses.clear()
            is_new_group = True
            continue

        line = line.strip("\n")
        new_elements = list(line)

        if is_new_group:
            responses.update(new_elements)
            is_new_group = False

        # overwrite `responses` w/ the intersection
        # of prev and cur sets
        responses.intersection_update(set(new_elements))

    return count


if __name__ == "__main__":
    with open("data.txt") as f:
            data = f.readlines()

    print("Part one:", part_one(data))
    print("Part two:", part_two(data))
