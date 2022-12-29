# Day 12: Hill Climbing Algorithm
# https://adventofcode.com/2022/day/12

from typing import List, Tuple, Deque, Optional
from collections import deque
import math

def part_one(data: List[str], start: Optional[Tuple] = None) -> int:
    """
    Return the smallest number of steps between "S" to "E".

    Each cell on the grid is a char from "a-z", and steps
    are only allowed between chars that are less than, or at
    most one step greater than, the current char.
    """
    HEIGHT = len(data)
    WIDTH = len(data[0])
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    deque_of_paths: Deque = deque()
    seen = set()

    if not start:
        for r, line in enumerate(data):
            for c, value in enumerate(line):
                if value == "S":
                    start = (0, r, c)

    deque_of_paths.append(start)

    while deque_of_paths:
        steps, x, y = deque_of_paths.popleft()
        cur_char = data[x][y] if data[x][y] != "S" else "a"

        for r, c in directions:
            nx = x + r
            ny = y + c

            if (
                0 <= nx < HEIGHT
                and 0 <= ny < WIDTH
                and (nx, ny) not in seen
                and ord(data[nx][ny]) - ord(cur_char) <= 1
            ):
                seen.add((nx, ny))

                if data[nx][ny] == "E":
                    if data[x][y] in ["y", "z"]:  # "E" char is read as a "z".
                        return steps + 1
                    else:
                        seen.remove((nx, ny))

                deque_of_paths.append((steps + 1, nx, ny))

    return math.inf  # Returning inf makes part two easier.


def part_two(data: List[str]) -> int:
    """
    Return the shortest path to "E" for any "a" point.
    """
    shortest_path = math.inf
    for r, line in enumerate(data):
        for c, value in enumerate(line):
            if value == "a":
                cur_path = part_one(data, start=(0,r,c))
                shortest_path = min(shortest_path, cur_path)

    return shortest_path


if __name__ == "__main__":
    with open("data.txt") as f:
        data = [line.strip() for line in f.readlines()]

    print("Part one:", part_one(data))
    print("Part two:", part_two(data))
