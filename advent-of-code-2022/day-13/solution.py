# Day 13: Distress Signal
# https://adventofcode.com/2022/day/13

from typing import List, Union
from collections import defaultdict
from functools import cmp_to_key


def part_one(data: List[str]) -> int:
    """
    Return the sum of the idices of pairs that are properly ordered.
    """
    dict_of_pairs = defaultdict(list)
    pair_index = 1
    result = 0

    for line in data:
        if line == "\n":
            pair_index += 1
        else:
            evaluated_line: List[Union[int, List]] = [eval(line)]
            dict_of_pairs[pair_index].append(evaluated_line)

    for key, (left, right) in dict_of_pairs.items():
        if is_pair_ordered(left, right) == -1:
            result += key

    return result


def part_two(data: List[str]) -> int:
    """
    Return product of the indices of each decoder-key after sorting data.
    """
    evaluated_data: List[Union[int, List]] = [
        eval(line) for line in data if line != "\n"
    ]
    decode_key_1, decode_key_2 = [[2]], [[6]]
    evaluated_data.extend([decode_key_1, decode_key_2])
    sorted_list = sorted(
        evaluated_data,
        key=cmp_to_key(
            lambda x, y: is_pair_ordered([x], [y])
        ),  # put x, y in list to satisfy mypy
    )
    return (sorted_list.index(decode_key_1) + 1) * (sorted_list.index(decode_key_2) + 1)


def is_pair_ordered(
    left_list: List[Union[int, List]], right_list: List[Union[int, List]]
) -> int:
    """
    A comparison function; compares two items, `left` and `right`.

    Return:
        -1 if `left` is smaller than `right`.
        1 if `left` is bigger than `right`.
        0 if `left` is the same as `right`.
    """
    LEFT_LENGTH = len(left_list)
    RIGHT_LENGTH = len(right_list)
    index = 0
    while index < LEFT_LENGTH and index < RIGHT_LENGTH:
        left_item = left_list[index]
        right_item = right_list[index]

        if left_item != right_item:
            if isinstance(left_item, int) and isinstance(right_item, int):
                if left_item < right_item:
                    return -1
                elif left_item > right_item:
                    return 1

            elif isinstance(left_item, list) and isinstance(right_item, list):
                return is_pair_ordered(left_item, right_item)

            elif isinstance(left_item, list) and isinstance(right_item, int):
                right_list[index] = [right_item]
                continue

            elif isinstance(left_item, int) and isinstance(right_item, list):
                left_list[index] = [left_item]
                continue

        index += 1

    if index == LEFT_LENGTH and index < RIGHT_LENGTH:
        return -1
    elif index < LEFT_LENGTH and index == RIGHT_LENGTH:
        return 1
    return 0


if __name__ == "__main__":
    with open("data.txt") as f:
        data = f.readlines()

    print("Part one:", part_one(data))
    print("Part two:", part_two(data))
