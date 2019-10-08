#https://en.wikipedia.org/wiki/Mass_fraction_(chemistry)
#https://www.quora.com/What-is-the-direct-formula-for-converting-mole-fraction-to-mass-percent
wfrac_ag=float(input("Enter the weight fraction of Ag:   "))
wag=wfrac_ag
wfrac_cu=float(input("Enter the weight fraction of Cu:   "))
wcu=wfrac_cu
wsn=1.0-(wcu+wag)
#Molmass_cu=input("Enter the molar mass of Cu:   ")
#mcu=Molmass_cu
#Molmass_sn=input("Enter the molar mass of Sn:   ")
#msn=Molmass_sn
mag=107.8682E-03 #kg/mol
mcu=63.546E-03 #kg/mol
msn=118.71E-03 #kg/mol
rag=wag/mag
rcu=wcu/mcu
rsn=wsn/msn
def sigmar(*args):
    sum = 0
    for arg in args:
        sum += arg
    return sum
denominator=sigmar(rag,rcu,rsn)
print("denominator")
print(sigmar(rag,rcu,rsn))
def molfraction(x):
    return x/denominator
molfrac_ag=molfraction(rag)
molfrac_cu=molfraction(rcu)
molfrac_sn=molfraction(rsn)
print("mole fraction of Ag is")
print(molfrac_ag)
print("mole fraction of Cu is")
print(molfrac_cu)
print("mole fraction of Sn is")
print(1.0-molfrac_ag-molfrac_cu)
########Computation of effective molecular weight########
def molweight(x1,m1,x2,m2,x3,m3):
    effective_wt=x1*m1+x2*m2+x3*m3
    return effective_wt
#########################################################
alloy_mw=molweight(molfrac_ag,mag,molfrac_cu,mcu,molfrac_sn,msn)
##################################################################
print("weight of sac in kg/mol is:",alloy_mw)


