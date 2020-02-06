# Day 2: 1202 Program Alarm Pt. 2
# https://adventofcode.com/2019/day/2
from solutionPart1 import opcode1, opcode2
from itertools import product

# Code terminology updated according to problem specifications
def noun_verb_locator(src):
    '''Transform memory based on opcodes and return position zero.'''
    memory = src
    instruction_pointer = 4
    for i in range(0, len(memory), instruction_pointer):
        adr = i
        instruction = memory[adr]
        params = memory[adr+1:adr+4]
        if instruction == 99:
            break
        elif instruction == 1:
            opcode1(memory, params)
        elif instruction == 2:
            opcode2(memory, params)
    return(memory[0])
    
if __name__ == '__main__':
    desired_output = 19690720
    noun_verb_pairs = list(product(list(range(0,100)), repeat=2))

    # Try noun/verb combinations against desired output
    for p in noun_verb_pairs:
        source = open('day_2/data.txt', 'r')
        memory = [list(map(int, i.split(','))) for i in source][0]
        source.close()
        memory[1] = p[0]
        memory[2] = p[1]

        # Solution
        if noun_verb_locator(memory) == desired_output:
            print(100*p[0]+p[1])

