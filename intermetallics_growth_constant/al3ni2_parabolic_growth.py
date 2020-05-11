Reference: Schoo et al, Defect and Diffusion Forum, 143-147 (2009), pp. 631-636
########################
import numpy as np
######Parabolic growth rate with temperature dependent growth rate constant arrheniusk#######
def arrheniusk(k0,Qa,R,T):
    exponent_term=np.exp(-Qa/(R*T))
    return k0*exponent_term
# numerical data file of phases
