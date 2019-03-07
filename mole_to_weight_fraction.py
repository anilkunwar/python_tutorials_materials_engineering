# https://www.engr.colostate.edu/CBE101/topics/exercise_solutions/exercise_mole_fraction_to_mass_fraction.html
# The code can be validated with the calculation made in the above website
xfrac_o2=input("Enter the mole fraction of O2 (nO2):   ")
xo2=xfrac_o2
xfrac_n2=input("Enter the mole fraction of N2 (nN2):   ")
xn2=xfrac_n2
xco2=1.0-xo2-xn2
Molmass_o2=input("Enter the molar mass of O2:   ")
mo2=Molmass_o2
Molmass_n2=input("Enter the molar mass of N2:   ")
mn2=Molmass_n2
Molmass_co2=input("Enter the molar mass of CO2:   ")
mco2=Molmass_co2
ro2=xo2*mo2
rn2=xn2*mn2
rco2=xco2*mco2

def sigmar(*args):
    sum = 0
    for arg in args:
        sum += arg
    return sum
denominator=sigmar(ro2,rn2,rco2)
print("denominator")
print(sigmar(ro2,rn2,rco2))
def massfraction(x):
    return x/denominator
massfrac_o2=massfraction(ro2)
massfrac_n2=massfraction(rn2)
massfrac_co2=massfraction(rco2)
print("mole fraction of O2 is")
print(massfrac_o2)
print("mole fraction of N2 is")
print(massfrac_n2)
print("mole fraction of CO2 is")
print(1.0-massfrac_o2-massfrac_n2)


