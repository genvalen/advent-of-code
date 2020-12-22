def binary_parser(start, end, directions):
    """
    Use binary search to traverse a range determined by input. \
    Traverse directions; for each char in direction, split the \ 
    range in two and move into the half determiend by char: \
    F, B, L, R -> front, back, left, right.   
    """
    left, right = start, end
    pointer = 0
    mid = 0

    while pointer < len(directions):
        mid = left + (right-left)//2

        # choose lower half
        if directions[pointer] in "FL":
            right = mid
        
        # choose upper half
        elif directions[pointer] in "BR":
            left = mid + 1

        pointer += 1

    return left

def get_seat_ID(directions):
    #extract row/col directions
    row_dirs = directions[:7]
    col_dirs = directions[7:]

    # identify correct row, col, and seat ID
    row = binary_parser(0, 127, row_dirs)
    col = binary_parser(0, 7, col_dirs)
    id_ = row*8 + col

    return id_


def part_one(data):
    max_id = 0

    for line in data:
        cur_id = get_seat_ID(line)
        max_id = max(max_id, cur_id)

    return max_id
    
def part_two(data):
    max_id = part_one(data)
    min_id = max_id 
    ids_seen = set()

    for line in data:
        cur_id = get_seat_ID(line)
        ids_seen.add(cur_id)
        min_id = min(min_id, cur_id)

    missing_id = set(range(min_id, max_id+1)).difference(ids_seen).pop()

    return missing_id



if __name__ == "__main__":
    with open("data.txt") as f:
        data = f.readlines()
    # with open("output.txt", "a") as f:
    #     f.write(str(part_one(data)) + "\n")

    print("Part one:", part_one(data))
    print("Part two:", part_two(data))



    