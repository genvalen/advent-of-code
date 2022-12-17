# Day 8: Treetop Tree House
# https://adventofcode.com/2022/day/8

from typing import List


def part_one(data: List[str]) -> int:
    HEIGHT: int = len(data)
    WIDTH: int = len(data[0].strip())
    trees_seen = set()
    total = 0

    prev_row: List[int] = [-1] * WIDTH
    for r, line in enumerate(data):
        trees = list(map(int, list(line.strip())))
        prev_max_tree = -1

        for c, cur_tree in enumerate(trees):

            # Find trees visible starting from the left.
            if cur_tree > prev_max_tree:
                prev_max_tree = cur_tree
                trees_seen.add((r, c))

            # Find trees visible starting from the top.
            if cur_tree > prev_row[c]:
                prev_row[c] = cur_tree
                trees_seen.add((r, c))

    prev_row = [-1] * WIDTH
    for r, line in enumerate(reversed(data)):
        trees = list(map(int, list(line.strip())))
        prev_max_tree = -1

        for c, cur_tree in enumerate(reversed(trees)):
            adjusted_r = (HEIGHT - r) - 1
            adjusted_c = (WIDTH - c) - 1

            # Find trees visible starting from the right.
            if cur_tree > prev_max_tree:
                prev_max_tree = cur_tree
                trees_seen.add((adjusted_r, adjusted_c))

            # Find trees visible starting from the bottom.
            if cur_tree > prev_row[c]:
                prev_row[c] = cur_tree
                trees_seen.add((adjusted_r, adjusted_c))

    total += len(trees_seen)

    return total


def part_two(data: List[str]) -> int:
    coords: List[List[int]] = [list(map(int, list(line.strip()))) for line in data]
    HEIGHT = len(coords)
    WIDTH = len(coords[0])

    max_scenic_view = -1

    for r in range(HEIGHT):
        for c in range(WIDTH):
            tree = coords[r][c]
            cur_scenic_view = 1

            # trees from left to current col.
            trees = 0
            for i in range(0, c):
                cur = coords[r][i]

                if cur >= tree:
                    trees = 0
                    trees += 1

                elif cur < tree:
                    trees += 1

            # trees from current col to right.
            trees = 0
            for i in range(c + 1, WIDTH):
                cur = coords[r][i]

                if cur < tree:
                    trees += 1

                elif cur >= tree:
                    trees += 1
                    break

            cur_scenic_view *= trees

            #  trees from from the top and down to current row.
            trees = 0
            for i in range(0, r):
                cur = coords[i][c]

                if cur >= tree:
                    trees = 0
                    trees += 1

                elif cur < tree:
                    trees += 1

            cur_scenic_view *= trees

            # trees from current row and down to the bottom.
            trees = 0
            for i in range(r + 1, HEIGHT):
                cur = coords[i][c]

                if cur < tree:
                    trees += 1

                if cur >= tree:
                    trees += 1
                    break

            cur_scenic_view *= trees

            max_scenic_view = max(max_scenic_view, cur_scenic_view)

    return max_scenic_view


if __name__ == "__main__":
    with open("data.txt") as f:
        data = f.readlines()

    with open("output.txt", "a") as f:
        f.write("Part one: " + str(part_one(data)) + "\n")
        f.write("Part two: " + str(part_two(data)) + "\n")

    print("Part one:", part_one(data))
    print("Part two:", part_two(data))
