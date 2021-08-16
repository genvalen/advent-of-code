def part_one(nums: list, total: int = 2020) -> int:
    nums.sort()
    seen = set()

    for num in nums:
        if not seen:
            seen.add(num)
            continue

        target = total - num

        if target in seen:
            return num * target

        seen.add(num)

    return


def part_two(nums: list, total: int = 2020) -> int:
    nums.sort()

    for num in nums:
        two_sum_target = total - num
        sub_list = nums.copy()
        sub_list.remove(num)
        two_sum_result = part_one(sub_list, two_sum_target)

        if two_sum_result:
            return num * two_sum_result

    return


if __name__ == "__main__":
    with open("data.txt") as f:
        data = [int(line.strip()) for line in f]

    print("Part one:", part_one(data))
    print("Part two:", part_two(data))
 