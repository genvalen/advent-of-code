# Day 2: 1202 Program Alarm Pt. 1
# https://adventofcode.com/2019/day/2
def opcode1(src, seg):
    '''Transforms source array. Adds src values at seg positions 0-1 and
    stores sum in src at seg position 2.'''
    s = 0
    for i in seg[:2]:
        s += src[i]
    src[seg[-1]] = s

def opcode2(src, seg):
    '''Transforms source array. Multiplies src values at seg positions 0-1 
    and stores product in src at seg position 2.'''
    p = 1
    for i in seg[:2]:
        p *= src[i]
    src[seg[-1]] = p


if __name__ == '__main__':
    source = open('day_2/data.txt', 'r')

    # Splice s at 0 to cancel list-nesting
    s = [list(map(int, i.split(','))) for i in source][0]
    source.close()

    # Restore computer to "1202 program alarm" settings
    s[1] = 12
    s[2] = 2

    # Run program
    for i in range(0, len(s), 4):
        if s[i] == 99:
            break
        elif s[i] == 1:
            opcode1(s, s[i+1:i+4])
        elif s[i] == 2:
            opcode2(s, s[i+1:i+4])
        else:
            print("sequence out of order")

    # solution
    print("Value at position 0 after program halts:", s[0])