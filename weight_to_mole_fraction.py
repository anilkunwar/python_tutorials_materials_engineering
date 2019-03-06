#https://en.wikipedia.org/wiki/Mass_fraction_(chemistry)
#https://www.quora.com/What-is-the-direct-formula-for-converting-mole-fraction-to-mass-percent
wfrac_cu=input("Enter the weigth fraction of Cu:   ")
wcu=wfrac_cu
wsn=1.0-wcu
Molmass_cu=input("Enter the molar mass of Cu:   ")
mcu=Molmass_cu
Molmass_sn=input("Enter the molar mass of Sn:   ")
msn=Molmass_sn
rcu=wcu/mcu
rsn=wsn/msn

def sigmar(*args):
    sum = 0
    for arg in args:
        sum += arg
    return sum
denominator=sigmar(rcu,rsn)
print("denominator")
print(sigmar(rcu,rsn))
def molfraction(x):
    return x/denominator
molfrac_cu=molfraction(rcu)
molfrac_sn=molfraction(rsn)
print("mole fraction of Cu is")
print(molfrac_cu)
print("mole fraction of Sn is")
print(1.0-molfrac_cu)


