# Giant Squid
# https://adventofcode.com/2021/day/4

from typing import List


def is_winning_row(start: int, boards: List[int]) -> bool:
    """Return whether row starting at `start` index is a winner."""
    count = 0
    for i in range(start, start + 5):
        if boards[i] == -1:
            count += 1
    return count == 5


def is_winning_column(start: int, boards: List[int]) -> bool:
    """Return whether colunm starting at `start` index is a winner."""
    count = 0
    for i in range(start, start + 21, 5):
        if boards[i] == -1:
            count += 1
    return count == 5


def mark_boards(num: int, boards: List[int]):
    "Mark each instance of the specified number with -1."
    for i, x in enumerate(boards):
        if x == num:
            boards[i] = -1


def find_winning_board(nums: List[int], boards: List[int], win_pos: int = 1) -> int:
    """Return the board that wins at the specified "win position".
    By default, return the first board that wins."""
    MAX_BOARDS = 100
    starting_points = []
    winning_num = None
    winning_board = None

    # mark start of each board (every 25 indices is a new board)
    point = 0
    while point < len(boards):
        starting_points.append(point)
        point += 25

    # begin playing bingo
    for num in nums:
        mark_boards(num, boards)

        # Check for / discard any winning boards
        for point in list(starting_points):
            winning_row, winning_col = False, False

            for row in range(point, point + 21, 5):
                if is_winning_row(row, boards):
                    winning_row = True

            for column in range(point, point + 5):
                if is_winning_column(column, boards):
                    winning_col = True
            
            if winning_row or winning_col:
                starting_points.remove(point)  # discard winning board

                # if winner is at the correct "win position", end program
                if MAX_BOARDS - len(starting_points) == win_pos:
                    winning_board = point
                    winning_num = num

        if winning_num:
            break

    return winning_board, winning_num


def score(nums: List[int], boards: List[int], win_position: int = 1):
    """Return score of the winning board: sum the unmarked numbers
    and multipy total by the winning num."""
    winning_board_idx, winning_num = find_winning_board(nums, boards, win_position)
    total = 0

    for i in range(winning_board_idx, winning_board_idx + 25):
        total += boards[i] if boards[i] != -1 else 0

    return total * winning_num


if __name__ == '__main__':
    with open("data.txt") as f:
        data = f.readlines()
        bingo_nums = list(map(int, data[0].strip().split(",")))
        board_data = list(map(lambda x: x.strip().split(), data[1:]))
        board_data = [num for row in board_data for num in row]
        board_data = list(map(int, board_data))

    print("Part one:", score(bingo_nums, board_data))
    print("Part two:", score(bingo_nums, board_data, 100))
