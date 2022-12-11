# Day 6: Tuning Trouble
# https://adventofcode.com/2022/day/6

from collections import defaultdict


def part_one(datastream: str, msg_length=4) -> int:
    d: defaultdict = defaultdict(int)
    leading_char = 0

    for pos, char in enumerate(datastream, 1):
        if pos < msg_length:
            d[char] += 1
            continue

        d[char] += 1

        if len(d.keys()) == msg_length and sum(d.values()) == msg_length:
            return pos

        d[datastream[leading_char]] -= 1

        if d[datastream[leading_char]] == 0:
            d.pop(datastream[leading_char])

        leading_char += 1

    return -1


def part_two(datastream: str) -> int:
    return part_one(datastream, 14)


if __name__ == "__main__":
    with open("data.txt") as f:
        data = f.read()

    with open("output.txt", "a") as f:
        f.write("Part one: " + str(part_one(data)) + "\n")
        f.write("Part two: " + str(part_two(data)) + "\n")

    print("Part one:", part_one(data))
    print("Part two:", part_two(data))
