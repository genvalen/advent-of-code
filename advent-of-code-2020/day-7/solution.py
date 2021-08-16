# Handy Haversacks
# https://adventofcode.com/2020/day/7

def part_one(data: list, target: str = "shiny gold bag") -> int:
    """Immplements topological sort.

    Returns the number of unique bags that are able to hold
    (directly or indirectly) the target bag.
    """
    bag_types = dict()
    contains_target = set()
    count = 0

    for line in data:
        line = line.strip()
        key, value = line.split(" contain ")

        # remove 's' from '...bags' to make singular, not plural
        # for consistency when traversing outer layers in the sort
        key = key[:-1]

        if target in value:
            contains_target.add(key)
            count += 1
            continue

        bag_types[key] = value

    while contains_target:
        bag = contains_target.pop()

        seen = set()
        for k, v in bag_types.items():
            if bag in v:
                count += 1
                seen.add(k)
                contains_target.add(k)

        #remove bags from dict
        for bag in seen:
            del bag_types[bag]

    return count


def part_two(data, target: str = "shiny gold bag") -> int:
    """Returns the number of unique bags that the target bag contains."""
    bags_to_search = dict()

    for line in data:
        line = line.strip()
        key, value = line.split(" contain ")

        if target in key:
            for bag in value.split(", "):
                if "no other bags." in bag:
                    break

                quantity, color = bag.split(" ", 1)
                color = color.strip(".")
                bags_to_search[color] = int(quantity)

            break

    # adjust total so that outermost bag (intitial target)
    # is not included in the final count. Otherwise,
    # counts reflect number of bags contained within a bag, plus itself.
    total = 0 if target == "shiny gold bag" else 1

    for color, quantity in bags_to_search.items():
        total += quantity * part_two(data, color)

    return total


if __name__ == "__main__":
    with open("data.txt") as f:
            data = f.readlines()

    print("Part one:", part_one(data))
    print("Part two:", part_two(data))
