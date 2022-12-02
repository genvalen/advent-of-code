# Day 1: Calorie Counting
# https://adventofcode.com/2022/day/1

from typing import List, DefaultDict
from collections import defaultdict


def solution(data: List[str], n: int = 1) -> int:
    """
    Return the sum of the n largest values of calories
    calculated from the input data.
    """
    calories: DefaultDict[int, int] = defaultdict(int)

    cur_elf_total_calories = 0
    for line in data:
        if line == "\n":
            calories[cur_elf_total_calories] += 1
            cur_elf_total_calories = 0
            continue

        cur_elf_total_calories += int(line)

    total_calories = 0
    for _ in range(n):
        max_calories_found = max(calories.keys())
        total_calories += max_calories_found
        calories[max_calories_found] -= 1

        if calories[max_calories_found] == 0:
            calories.pop(max_calories_found)

    return total_calories


if __name__ == "__main__":
    with open("data.txt") as f:
        data = f.readlines()

    print("Part one:", solution(data))
    print("Part two:", solution(data, 3))
