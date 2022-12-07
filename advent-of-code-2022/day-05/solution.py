# Day 5: Supply Stacks
# https://adventofcode.com/2022/day/5

from typing import List, Dict
from collections import defaultdict, deque


def part_one(data: List[str]) -> str:
    CRATE_INFO = data[:9]
    INSTRUCTIONS = data[10:]

    stack_dict = build_initial_map_of_crates(CRATE_INFO)

    for instruction in INSTRUCTIONS:
        if instruction.split():
            _, iterations, _, stack_a, _, stack_b = instruction.split()

        for _ in range(int(iterations)):
            stack_dict[stack_b].appendleft(
                    stack_dict[stack_a].popleft()
                )

    result = ""
    for stack in range(1, len(stack_dict.keys()) + 1):
        result += stack_dict[str(stack)].popleft()

    return result


def part_two(data: List[str]) -> str:
    CRATE_INFO = data[:9]
    INSTRUCTIONS = data[10:]

    stack_dict = build_initial_map_of_crates(CRATE_INFO)

    for instruction in INSTRUCTIONS:
        if instruction.split():
            _, iterations, _, stack_a, _, stack_b = instruction.split()

        tmp_deque: deque = deque()
        for _ in range(int(iterations)):
            tmp_deque.appendleft(
                    stack_dict[stack_a].popleft()
                )

        for _ in range(int(iterations)):
            stack_dict[stack_b].appendleft(
                    tmp_deque.popleft()
                )

    result = ""
    for stack in range(1, len(stack_dict.keys()) + 1):
        result += stack_dict[str(stack)].popleft()

    return result


def build_initial_map_of_crates(data: List[str]) -> Dict[str, deque]:
    CRATE_ROWS: str = data.pop()

    stack_dict: Dict[str, deque] = defaultdict(deque)

    for line in data:
        # line = line.replace(" ", ".")
        for i, c in enumerate(line):
            if c == "[":
                crate_value: str = line[i + 1]
                crate_row: str = CRATE_ROWS[i + 1]

                stack_dict[crate_row].append(crate_value)

    return stack_dict


if __name__ == "__main__":
    with open("data.txt") as f:
        data = f.readlines()

    with open("output.txt", "a") as f:
        f.write("Part one: " + str(part_one(data)) + "\n")
        f.write("Part two: " + str(part_two(data)) + "\n")

    print("Part one:", part_one(data))
    print("Part two:", part_two(data))
