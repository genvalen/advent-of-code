# Day 2: Rock Paper Scissors
# https://adventofcode.com/2022/day/2

from typing import List, Dict, Any


def part_one(data: List[str]) -> int:
    score = 0
    for line in data:
        opponent_move, player1_move = line.strip().split()
        score += get_player1_score(opponent_move, player1_move)

    return score


def part_two(data: List[str]) -> int:
    score = 0
    for line in data:
        opponent_move, strategy = line.strip().split()
        player1_move: str = get_suggested_response(opponent_move, strategy)
        score += get_player1_score(opponent_move, player1_move)

    return score


def get_suggested_response(p1_selection: str, strategy: str) -> str:
    """
    Return the move that player1 should select based on the given strategy.
    """
    guide: Dict[Any, Any] = {"A": 1, "B": 2, "C": 3, 1: "A", 2: "B", 3: "C"}

    p1: int = guide[p1_selection]
    p2: int

    if strategy == "X":  # fabricate a loss -- select value smaller than p1.
        p2 = 3 if (p1 - 1) % 3 == 0 else (p1 - 1) % 3
    elif strategy == "Y":  # fabricate a draw
        p2 = p1
    elif strategy == "Z":  # fabricate a win -- select value greater than p1.
        p2 = 3 if (p1 + 1) % 3 == 0 else (p1 + 1) % 3

    return guide[p2]


def get_player1_score(p1_selection: str, p2_selection: str) -> int:
    """
    Return the score that player1 gets when competeing against player2.

    In the score guide:
        A/X = Rock
        B/Y = Paper
        C/Z = Scissors

    The score for a single round is the score for the
    shape selected: (1 for Rock, 2 for Paper, and 3 for Scissors)
    plus the score for the outcome of the round:
    (0 if you lost, 3 if the round was a draw, and 6 if you won).
    """
    score_guide: Dict[str, int] = {
        "A": 1,
        "B": 2,
        "C": 3,
        "X": 1,
        "Y": 2,
        "Z": 3,
    }

    p1: int = score_guide[p1_selection]
    p2: int = score_guide[p2_selection]
    score: int = 0

    if p1 == p2:
        score += 3
    elif p2 - p1 == 1 or p2 - p1 == -2:
        score += 6

    score += p2

    return score


if __name__ == "__main__":
    with open("data.txt") as f:
        data = f.readlines()

    with open("output.txt", "a") as f:
        f.write("Part one: " + str(part_one(data)) + "\n")
        f.write("Part two: " + str(part_two(data)) + "\n")

    print("Part one:", part_one(data))
    print("Part two:", part_two(data))
