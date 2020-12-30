def part_one(data):
    """
    Use input data to mimic adjaceny list;\
    apply topological sorting to filter through adj-list(dict); \
    Return num of bags which directly/indirectly hold target.
    """
    bags = dict()
    target = "shiny gold bag"
    contains_target = set()
    count = 0

    for line in data:
        line = line.strip()
        key, value = line.split(" contain ")

        # make key (bag-color) singular, !plural
        key = key[:-1] 

        # identify bags that directly contain target
        # add all other bags into dict
        if target in value:
            contains_target.add(key)
            count += 1
            continue

        bags[key] = value

    while contains_target:
        bag = contains_target.pop()

        visited = set()
        for k, v in bags.items():
            if bag in v:
                count += 1
                visited.add(k)
                contains_target.add(k)
                
        #remove visited bags from dict
        for bag in visited:
            del bags[bag]

    return count
                

def part_two(data):
    pass


if __name__ == "__main__":
    with open("sample2.txt") as f:
            data = f.readlines()
    # with open("output.txt", "a") as f:
    #     f.write(str(part_one(data)) + "\n")

    print("Part one:", part_one(data))
    # print("Part two:", part_two(data))