#Reference: Schoo et al, Defect and Diffusion Forum, 143-147 (2009), pp. 631-636
########################
import numpy as np
######Parabolic growth rate with temperature dependent growth rate constant arrheniusk#######
def arrheniusk(k0,Qa,R,T):
    exponent_term=np.exp(-Qa/(R*T))
    return k0*exponent_term
#############################################
def xparabolic(x0,k,t,n):
    pow_term=np.power(t,n)
    return x0+k*pow_term
###############################################
# numerical data for growth constant calculation and layer thickness
k0=3.7E-06 #m^2/s
Qa= 1.26E+05 #J/mol
R=8.31 # J/mol K
T = 800 # K
x0 = 2.0E-08 # m
t = 60 # s
n = 0.5 # diffusion based parabolic growth , no units
###############calculation of growth constant#############################
kcalc = arrheniusk(k0,Qa,R,T)
print("Growth constant (m^2/s) at the temperature=",kcalc)
###############calculation of layer thickness at t############################
xt = xparabolic(x0,kcalc,t,n)
print("Al3Ni2 IMC layer thickness (m) at t=",xt)

