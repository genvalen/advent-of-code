def part_one(nums):
        for i in nums:
            for j in nums[1:]:
                if i + j == 2020:
                    return i * j


def part_two(nums):
        for i in nums:
            for j in nums[1:]:
                for k in nums[2:]:
                    if i + j + k == 2020:
                        return i * j * k


with open("advent-of-code-2020/day-1/data.txt") as f:
        data = [int(line.strip()) for line in f]

print("Part one:", part_one(data))
print("Part two:", part_two(data))