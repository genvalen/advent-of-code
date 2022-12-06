# Day 3: Rucksack Reorganization
# https://adventofcode.com/2022/day/3

from typing import List, Set, Dict


def part_one(data: List[str]) -> int:
    """
    Find the item that appears in both compartments of each line.
    Return the sum of the priorities of those items.
    """
    priority_total = 0
    priority_map: Dict[str, int] = get_priority_map()

    for line in data:
        MID = len(line.strip()) // 2
        compartment1 = line[:MID]
        compartment2 = line[MID:]

        intersection_item = set(compartment1).intersection(compartment2).pop()
        priority_total += priority_map[intersection_item]

    return priority_total


def part_two(data: List[str]) -> int:
    """
    Find the item that appears in each three-elf group.
    Return the sum of the priorities of those items.
    """
    priority_total = 0
    group_member = 1
    group_intersection: Set[str] = set()
    priority_map: Dict[str, int] = get_priority_map()

    for line in data:
        line = line.strip()

        if group_member == 1:
            group_intersection.update(line)

        elif group_member == 2:
            group_intersection.intersection_update(line)

        else:
            group_intersection.intersection_update(line)
            item = group_intersection.pop()
            priority_total += priority_map[item]
            group_member = 0

        group_member += 1

    return priority_total


def get_priority_map() -> Dict[str, int]:
    """
    Return a mapping of alphabet letters and their priority number.
    """
    alphabet_priority_map: Dict[str, int] = {}

    # add uppercase alphabet (odinals 65-90)
    for num in range(65, 91):
        char = chr(num)
        alphabet_priority_map[char] = num - 38  # start letters at 27

    # add lowercase alphabet (ordinals 97-122)
    for num in range(97, 123):
        char = chr(num)
        alphabet_priority_map[char] = num - 96  # start letters at 1

    return alphabet_priority_map


if __name__ == "__main__":
    with open("data.txt") as f:
        data = f.readlines()

    print("Part one:", part_one(data))
    print("Part two:", part_two(data))
