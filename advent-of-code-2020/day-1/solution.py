# Report Repair
# https://adventofcode.com/2020/day/1

from typing import List, Set

def part_one(nums: List[int], total: int = 2020) -> int:
    nums.sort()
    seen: Set[int] = set()

    for num in nums:
        if not seen:
            seen.add(num)
            continue

        target = total - num

        if target in seen:
            return num * target

        seen.add(num)

    return -1


def part_two(nums: List[int], total: int = 2020) -> int:
    nums.sort()

    for num in nums:
        two_sum_target = total - num
        sub_list = nums.copy()
        sub_list.remove(num)
        two_sum_result = part_one(sub_list, two_sum_target)

        if two_sum_result:
            return num * two_sum_result

    return -1


if __name__ == "__main__":
    with open("data.txt") as f:
        data = [int(line.strip()) for line in f]

    print("Part one:", part_one(data))
    print("Part two:", part_two(data))
