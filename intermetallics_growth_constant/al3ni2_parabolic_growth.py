Reference: Schoo et al, Defect and Diffusion Forum, 143-147 (2009), pp. 631-636
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
# numerical data 
k0=3.7E-06 #m^2/s
Qa= 1.26E+05 #J/mol
R=
