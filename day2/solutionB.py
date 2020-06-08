# Day 2: 1202 Program Alarm Part 2
# https://adventofcode.com/2019/day/2
from solutionA import opcode1, opcode2
from itertools import product

# Similar script to part 1 main, but as a function;
# Function terminology changed according to AoC specifications
def noun_verb_locator(src):
    """Transform memory based on opcodes/instructions and return position zero."""
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
    noun_verb_pairs = list(product(range(0,100), repeat=2))

    # Reset computer memory for each noun/verb combination
    # and try against desired output
    for p in noun_verb_pairs:
        with open("day2/data.txt", "r") as source:
            memory = [list(map(int, i.split(','))) for i in source][0]
        # Update combos
        memory[1] = p[0]
        memory[2] = p[1]

        # If output matches desired output
        # print solution and break
        if noun_verb_locator(memory) == desired_output:
            print("Solution:", 100*p[0]+p[1])
            break
        