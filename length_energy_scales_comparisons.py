# For python3.6
# Outputs the magnitudes of functions at given values of length, energy and time scales
##########################################################################################
ls=float(input("Enter the length scale of the simulation (1E+6 for 1 um):   "))
length_scale=ls
es=float(input("Enter the energy scale of the simulation (6.24E+18 for JtoeV, 1.0E+6 for I uJ):   "))
energy_scale=es
ts=float(input("Enter the time scale of the simulation (1 for 1 s, 1000 for 1 ms):   "))
time_scale=ts
sigma_int=float(input("Enter the interface energy (J/m^2):   "))
sigma=sigma_int
delta_width=float(input("Enter the interface width in m:   "))
delta=delta_width
gamma_input=float(input("Enter the grain-grain energy gamma (J/m^2):   "))
gamma=gamma_input
kappa=0.75*(sigma*delta)*(energy_scale/length_scale)
print("kappa (e/l) is")
print(kappa)
mu=6.0*(sigma/delta)*energy_scale/length_scale**3
print("mu (e/l^3) is")
print(mu)
Vmcu=7.124E-06
Vmsn=16.29E-06
Vmimc=10.6E-06 #m^3/mol
############################
######Free energy density#######
def fchem(A,B,C,x,xeq,Vm):
    parabolic_term=0.5*A*(x-xeq)**2+B*(x-xeq)+C
    scaling=energy_scale/length_scale**3
    return scaling*parabolic_term/Vm
#cu_fchem_input=float(input("Enter Acu,Bcu,Ccu,x,xeq separated by commas:   ")
#https://stackoverflow.com/questions/37629828/typeerror-float-argument-must-be-a-string-or-a-number-not-list-python
#b = list(map(float, a[0].split("*")))
#b = [float(s) for s in a[0].split("*")]
#Acu,Bcu,Ccu,xcu,xcueq=float(input("Enter Acu,Bcu,Ccu,x,xeq separated by commas:").split(','))
#cu_fchem_input=input("Enter Acu,Bcu,Ccu,x,xeq separated by commas:")
#Acu,Bcu,Ccu,xcu,xcueq=list(map(float, input().split(',')))
#fcu=[float(s) for s in input().split(',')]
#Tuple for extracting values
#Acu,Bcu,Ccu,xcu,xcueq=(fcu[0],fcu[1],fcu[2],fcu[3],fcu[4])
Acu,Bcu,Ccu,xcu,xcueq=float(input("Acu:")), float(input("Bcu:")), float(input("Ccu:")), float(input("xcu:")), float(input("xcueq:"))
fchem_cu=fchem(Acu,Bcu,Ccu,xcu,xcueq,Vmcu)
print("fchem_cu (e/l^3) is")
print(fchem_cu)
#imc_fchem_input=input("Enter Aimc,Bimc,Cimc,x,xeq separated by commas:")
#Aimc,Bimc,Cimc,ximc,ximceq=[float(s) for s in input().split(',')]
Aimc,Bimc,Cimc,ximc,ximceq=float(input("Aimc:")), float(input("Bimc:")), float(input("Cimc:")), float(input("ximc:")), float(input("ximceq:"))
fchem_imc=fchem(Aimc,Bimc,Cimc,ximc,ximceq,Vmimc)
print("fchem_imc (e/l^3) is")
print(fchem_imc)
#print(fchem_cu)
#imc_fchem_input=input("Enter Asn,Bsn,Csn,x,xeq separated by commas:")
#Asn,Bsn,Csn,xsn,xsneq=[float(s) for s in input().split(',')]
Asn,Bsn,Csn,xsn,xsneq=float(input("Asn:")), float(input("Bsn:")), float(input("Csn:")), float(input("xsn:")), float(input("xsneq:"))
fchem_sn=fchem(Asn,Bsn,Csn,xsn,xsneq,Vmsn)
#fchem_sn=fchem(Asn,Bsn,Csn,xsn,xsneq,Vmsn)
print("fchem_sn (e/l^3) is")
print(fchem_sn)
#############################CH Mobility=Di/Ai###########################
print("Calculate all CH mobilities for use in AC mobility calculations")
def phase_mob(A,D):
    diffusivity_term=D/A
    scaling=length_scale**5/(energy_scale*time_scale)
    return scaling*diffusivity_term
#diffusivities=input("Enter Dcu, Dimc, Dsn separated by commas:")
#Dcu,Dimc,Dsn=[float(s) for s in input().split(',')]
Dcu,Dimc,Dsn=float(input("Dcu:")), float(input("Dimc:")), float(input("Dsn:"))
mobility_cu=phase_mob(Acu,Dcu)
mobility_imc=phase_mob(Aimc,Dimc)
mobility_sn=phase_mob(Asn,Dsn)
print("CH mob_cu (l^2 mol/e*t) is")
print(mobility_cu)
print("CH mob_imc (l^2 mol/e*t) is")
print(mobility_imc)
print("CH mob_sn (l^2 mol/e*t) is")
print(mobility_sn)
#############################AC Mobility=const*Mi*vm*mu/(kappa*(x1-x2)^2)###########################
def phase_lij(M1,M2,V1,V2,xeq1,xeq2):
    mobility_term=0.5*mu*(V1+V2)*(M1+M2)/(3*kappa*(xeq1-xeq2)**2)
    scaling=length_scale**3/(energy_scale*time_scale)
    return scaling*mobility_term
L_cu_eta=phase_lij(mobility_cu,mobility_imc,Vmcu,Vmimc,xcueq,ximceq)
L_sn_eta=phase_lij(mobility_sn,mobility_imc,Vmsn,Vmimc,xsneq,ximceq)
print("AC mob_cu_eta (l^3 mol/e*t) is")
print(L_cu_eta)
print("AC mob_sn_eta (l^2 mol/e*t) is")
print(L_sn_eta)
#####################This coding can be improved by usin list, arrays, tuples and dictionaries
#####################Eureka####################################################################






