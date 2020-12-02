# The Tyranny of the Rocket Equations Part 1
# https://adventofcode.com/2019/day/1
def fuel_calculator(mass):
    return int(mass)//3-2

modules = open('day1/data.txt', 'r')
fuel_per_mod = [fuel_calculator(m) for m in modules]
modules.close()
print("Sum of fuel requirements:", sum(fuel_per_mod))