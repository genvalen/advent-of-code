def part_one(database_info):
    valid = 0

    for range_, char, password in database_info:
        char = char.strip(":")

        if char in password:
            char_count = password.count(char)
            MIN, MAX = map(int, range_.split("-"))

            if char_count >= MIN and char_count <= MAX:
                valid += 1

    return valid


def part_two(database_info):
    valid = 0

    for positions, char, password in database_info:
        pos1, pos2 = map(lambda x: int(x)-1, positions.split("-")) #adjust for zero-index
        chars = [password[pos1], password[pos2]]

        if char.strip(":") in chars and chars[0] != chars[1]:
            valid += 1

    return valid


if __name__ == "__main__":
    with open("data.txt") as f:
        data = [line.split() for line in f]

    print("Part one:", part_one(data))
    print("Part two:", part_two(data))
