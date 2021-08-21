# Passport Processing
# https://adventofcode.com/2020/day/4

from typing import List

def part_one(data: List[str]) -> int:
    valid = 0
    eof_marker = ["\n"]

    for line in data + eof_marker:
        if validate_passport_categories(line):
            valid += 1

    return valid


def part_two(data: List[str]) -> int:
    valid = 0
    eof_marker = ["\n"]

    for line in data + eof_marker:
        if validate_passport_categories(line) and \
            validate_passport_values(line):
            valid += 1

    return valid


def validate_passport_categories(passport_details: str) -> bool:
    """Compare passport fields against required fields.
    Return True if all required fields are present.
    """

    FIELDS = {"byr", "iyr", "eyr", "hgt", "hcl", "cid", "ecl", "pid"}
    is_valid = set()

    for field in passport_details.split():
        is_valid.add(field[:3])

    if FIELDS.difference(is_valid) == set() or \
            FIELDS.difference(is_valid) == {"cid"}:
            return True

    return False


def validate_passport_values(passport_details: str) -> bool:
    """Run passport values against series of checks.
    Return True if all values pass checks.
    """
    result = []
    elements = passport_details.split()

    for key_value in elements:
        key, value = key_value.split(":")

        if key == "byr":
            result.append(1920 <= int(value) <= 2002)
        elif key == "iyr":
            result.append(2010 <= int(value) <= 2020)
        elif key == "eyr":
            result.append(2020 <= int(value) <= 2030)
        elif key == "hgt":
            num, unit = value[:-2], value[-2:]

            # catch instance where num captures an empty str
            if not num: num = "0"

            if unit == "cm":
                result.append(150 <= int(num) <= 193)
            else:
                result.append(59 <= int(num) <= 76)
        elif key == "hcl":
            result.append(len(value) == 7 \
                            and value[0] == "#" \
                            and all([bool(c) if c in "abcdef" else c.isdigit() for c in value[1:]]))
        elif key == "ecl":
            options = set(("amb", "blu", "brn", "gry", "grn", "hzl", "oth"))
            result.append(value in options)

        elif key == "pid":
            result.append(len(value) == 9 and value.isdigit())

    return all(result)


if __name__ == "__main__":
    with open("data.txt") as f:
        data = f.read().split("\n\n")

    print("Part one:", part_one(data))
    print("Part two:", part_two(data))
