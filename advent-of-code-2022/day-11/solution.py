# Day 11: Monkey in the Middle
# https://adventofcode.com/2022/day/11

from typing import List, Tuple, DefaultDict, NamedTuple, Deque, Union
from collections import defaultdict, namedtuple, deque


def part_one(data: List[str], rounds: int = 20) -> int:
    """
    Return the product of the activity of the two most active monkeys.
    """
    monkey_items_dict, monkey_notes_list = setup_monkeys(data)
    monkey_activity_record: List[int] = [0] * len(monkey_items_dict)

    for _ in range(rounds):

        for monkey, items in monkey_items_dict.items():
            note = monkey_notes_list[monkey]
            while items:
                monkey_activity_record[monkey] += 1  # record monkey activity
                item_worry_level = items.popleft()
                new_worry_level = compute_new_worry_level(
                    item_worry_level, note.operator, note.number
                )
                recipient_monkey = (
                    note.true_monkey
                    if new_worry_level % note.divisor == 0
                    else note.false_monkey
                )
                monkey_items_dict[recipient_monkey].append(new_worry_level)

    # Identify 2 most ative monkeys
    monkey_activity_record.sort()
    return monkey_activity_record[-1] * monkey_activity_record[-2]


def setup_monkeys(data: List[str]) -> Tuple[DefaultDict[int, Deque], List[NamedTuple]]:
    monkey_items: DefaultDict[int, Deque] = defaultdict(deque)
    monkey_notes: List[Note] = []
    monkey = -1

    Note = namedtuple(
        "Note",
        [
            "monkey_number",
            "operator",
            "number",
            "divisor",
            "true_monkey",
            "false_monkey",
        ],
    )

    operator: str
    number: Union[int, str]
    divisor: int
    true_monkey: int
    false_monkey: int

    for line in data:
        if "Monkey" in line:
            monkey += 1

        elif "items" in line:
            parsed_line = line.split(":")[1].split(",")
            items_list = list(map(int, parsed_line))
            monkey_items[monkey].extend(items_list)  # extend deque

        elif "Operation" in line:
            parsed_line = line.split("=")[1].split()
            operator, number = (
                parsed_line[1:] if parsed_line.count("old") == 1 else ["**", "_"]
            )
            if str.isdigit(number):
                number = int(number)

        elif "Test" in line:
            parsed_line = line.split()
            divisor = int(parsed_line[-1])

        elif "true" in line:
            parsed_line = line.split()
            true_monkey = int(parsed_line[-1])

        elif "false" in line:
            parsed_line = line.split()
            false_monkey = int(parsed_line[-1])

            note = Note(monkey, operator, number, divisor, true_monkey, false_monkey)
            monkey_notes.append(note)

    return monkey_items, monkey_notes


def compute_new_worry_level(old: int, operator: str, number: int) -> int:
    new_worry_level: int
    if operator == "**":
        new_worry_level = old ** 2
    elif operator == "*":
        new_worry_level = old * number
    elif operator == "+":
        new_worry_level = old + number
    return new_worry_level // 3


def part_two(data: List[str], rounds: int = 20) -> int:
    pass


if __name__ == "__main__":
    with open("data.txt") as f:
        data = f.readlines()

    with open("output.txt", "a") as f:
        f.write("Part one: " + str(part_one(data)) + "\n")
        f.write("Part two: " + str(part_two(data)) + "\n")

    print("Part one:", part_one(data))
    print("Part two:", part_two(data))
