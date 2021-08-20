# Handheld Halting 
# https://adventofcode.com/2020/day/8

def part_one(data: list) -> int:
    """Traverse a list in a specific order.

    Return the value of `acc` at the end of the traversal,
    or if there is a cycle, prior to reentering the cycle."""
    seen = set()
    index, acc = 0, 0

    while index not in seen and index < len(data):
        operation, offset = data[index].split()
        seen.add(index)

        if operation == "acc":
            acc += int(offset)

        # update index according to operation type
        index += int(offset) if operation == "jmp" else 1

    return acc


def part_two(data: list) -> int:
    """There is an unwanted cycle in the order of traversal provided.

    Swap exactly one operation (jmp -> nop or nop -> jmp) to remove the
    cycle, and then return the value of `acc` at the end of the traversal.
    """
    operation_swap = {"jmp": "nop", "nop": "jmp"}
    indicies = find_indicies_to_check(data)

    for i in indicies:
        data_cp = data.copy()
        operation, offset = data_cp[i].split()
        operation = operation_swap[operation]
        data_cp[i] = "{} {}".format(operation, offset)

        # check if this change resolves the cycle
        if not has_cycle(data_cp):
            data = data_cp
            break

    return part_one(data)


def find_indicies_to_check(data: list, target: set = ("jmp", "nop")) -> set:
    """Return reachable indices whose value is a target value."""
    index = 0
    seen, indicies = set(), set()

    while index not in seen:
        operation, offset = data[index].split()

        if operation in target:
            indicies.add(index)

        seen.add(index)

        # update index according to operation type
        index += int(offset) if operation == "jmp" else 1

    return indicies


def has_cycle(data: list) -> bool:
    """Return whether a cycle has been detected."""
    index = 0
    list_end = len(data) - 1
    seen = set()

    while index not in seen and index <= list_end:
        if index == list_end:
            return False

        operation, offset = data[index].split()
        seen.add(index)

        # update index according to operation type
        index += int(offset) if operation == "jmp" else 1

    return True


if __name__ == "__main__":
    with open("data.txt") as f:
            data = f.readlines()

    print("Part one:", part_one(data))
    print("Part two:", part_two(data))
