# The Tyranny of the Rocket Equations Pt. 2
def fuel_calculator(mass):
    f = int(mass)//3-2
    if f > 0:
        return(f + fuel_calculator(f))
    else:
        return(0)

modules = open('day_1/data.txt', 'r')
fuel_per_mod = [fuel_calculator(m) for m in modules]
modules.close()
print(sum(fuel_per_mod))
