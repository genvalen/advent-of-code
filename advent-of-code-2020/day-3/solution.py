def part_one(map, right=3, down=1):
    """Traverse map according to slope; return no. of times 
        coordinate lands on "#" symbol."""
    row_len, col_len = len(map), len(map[0])
    row, col = 0, 0 #starting coordinate
    count = 0

    while row < row_len:
        if map[row][col] == "#":
            count += 1

        # update coordinate     
        row += down
        col = (col + right) % col_len #wrap cols

    return count
    
def part_two(map, slopes=set):
    """Traverse map using slopes provided; 
        multiply result of all slopes. Return final product."""
    product = 1
    for right, down in slopes:
        result = part_one(map, right, down)
        product *= result 
    
    return product


if __name__ == "__main__":
    with open("data.txt") as f:
        data = [line.strip() for line in f]

    print("Part one:", part_one(data))

    slopes = {(1,1), (3,1), (5,1), (7,1), (1,2)}
    print("Part two:", part_two(data, slopes))