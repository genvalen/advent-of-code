def part_one(nums):
    seen = set()
    for num in nums:
        if not seen:
            seen.add(num)

        target = abs(2020 - num)

        if target in seen:
            return num * target
        
        seen.add(num)
        
    return -1



def part_two(nums):
    for i in nums:
        for j in nums[1:]:
            for k in nums[2:]:
                if i + j + k == 2020:
                    return i * j * k

if __name__ == "__main__":
    with open("data.txt") as f:
            data = [int(line.strip()) for line in f]

    print("Part one:", part_one(data))
    print("Part two:", part_two(data))
    