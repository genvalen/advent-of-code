# Handheld Halting 
# https://adventofcode.com/2020/day/8

def part_one(data: list) -> int:
    seen = set()
    index, acc = 0, 0

    while index not in seen:
        operation, offset = data[index].split()
        seen.add(index)

        if operation == 'jmp':
            index += int(offset)
            continue

        if operation == 'acc':
            acc += int(offset)
        
        index += 1

    return acc


def part_two(data):
    pass


if __name__ == '__main__':
    with open('data.txt') as f:
            data = f.readlines()

    # with open('output.txt', 'a') as f:
    #     f.write(str(part_one(data)) + '\n')

    print('Part one:', part_one(data))
    print('Part two:', part_two(data))
