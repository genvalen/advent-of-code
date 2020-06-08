# The Tyranny of the Rocket Equations Part 2
# https://adventofcode.com/2019/day/1
def fuel_calculator(mass):
    f = int(mass)//3-2
    if f > 0:
        return(f + fuel_calculator(f))
    else:
        return(0)

modules = open('day1/data.txt', 'r')
fuel_per_mod = [fuel_calculator(m) for m in modules]
modules.close()
print("Sum of fuel requirements:", sum(fuel_per_mod))
