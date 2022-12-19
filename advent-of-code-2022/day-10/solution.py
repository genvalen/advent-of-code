# Day 10: Cathode-Ray Tube
# https://adventofcode.com/2022/day/10

from typing import List


def part_one(data: List[str]) -> int:
    """
    Track the value of the x-register when updating the x-register takes two cycles
    and noop (no operation) takes one cycle. Return the sum of each product,
    cycle_number * x_register, where cycle_number % 40 == 20 or cycle_number == 20.
    """
    cycle_number = 0
    x_register = 1
    index = 0
    prev_value = 0
    result = 0
    skip_next_cycle = False

    while index < len(data):
        cycle_number += 1

        if cycle_number % 40 == 20 or cycle_number == 20:
            result += cycle_number * x_register

        if skip_next_cycle:
            skip_next_cycle = False
            x_register += prev_value
            continue

        instruction, *cur_value = data[index].strip().split()
        index += 1

        if instruction == "addx":
            skip_next_cycle = True
            prev_value = int(cur_value[0])

    return result


def part_two(data: List[str]) -> None:
    """
    Scan a CRT's lines from left to right/top to bottom, and time the CPU instructions
    and CRT drawing operations to produce an image on the CRT.
    https://www.youtube.com/watch?v=sJFnWZH5FXc
    """
    cycle_number = 0
    x_register = 1
    index = 0
    prev_value = 0
    skip_next_cycle = False
    crt_index = 0
    crt = [["x" for _ in range(40)] for _ in range(6)]

    while index < len(data):
        cycle_number += 1

        if skip_next_cycle:
            skip_next_cycle = False
            draw_pixel(crt_index, x_register, crt)
            crt_index += 1
            x_register += prev_value
            continue

        instruction, *cur_value = data[index].strip().split()
        index += 1

        if instruction == "addx":
            skip_next_cycle = True
            prev_value = int(cur_value[0])

        draw_pixel(crt_index, x_register, crt)
        crt_index += 1

    for row in crt:
        print("".join(row))


def draw_pixel(index: int, x_register: int, crt: List[List[str]]) -> None:
    """
    Draw on the CRT screen.

    If the index provided sits under the 3-pixel sprite (the x_register represents
    the sprite's middle pixel), draw "#" on the CRT screen. Else, draw ".".
    """
    sprite = [max(0, x_register - 1), x_register, min(39, x_register + 1)]
    row, col = divmod(index, 40)
    if index % 40 in sprite:
        crt[row][col] = "#"
    else:
        crt[row][col] = "."


if __name__ == "__main__":
    with open("data.txt") as f:
        data = f.readlines()

    print("Part one:", part_one(data))
    print("Part two:", part_two(data))
