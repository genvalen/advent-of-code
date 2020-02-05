# The Tyranny of the Rocket Equations Pt. 1
def fuel_calculator(mass):
    return int(mass)//3-2

modules = open('day_1/data.txt', 'r')
fuel_per_mod = [fuel_calculator(m) for m in modules]
modules.close()
print(sum(fuel_per_mod))