########################
# Reference data: A Lis et al (2014), Journal of Alloys and Compounds vol. 617, pp. 763-773.
########################
import numpy as np
######Arrhenius Diffusivity#######
def arrdiff(d0,Qa,R,T):
    exponent_term=np.exp(-Qa/(R*T))
    return d0*exponent_term
# numerical data file of phases
filename_phases="constants.txt"
# Load data from tsv file: data
data_phases=np.loadtxt(filename_phases, delimiter=",", skiprows=1, 
                  usecols=[0,1,2,3,4,5])
d0fcc=data_phases[0]
d0imc=data_phases[1]
d0bct=data_phases[2]
Qafcc=data_phases[3]
Qaimc=data_phases[4]
Qabct=data_phases[5]
########################################
R=8.31 #J/molK
T1=393.15 #K 120 oC
T2=423.15 #K 150 oC
#####Compute diffusivity of the phases####################
###########Print the diffusivities###############3
################T1#########################################
difft1_fcc=arrdiff(d0fcc,Qafcc,R,T1)
print("Dfcc(m^2s^-1),393K=",difft1_fcc)
difft1_imc=arrdiff(d0imc,Qaimc,R,T1)
print("Dimc(m^2s^-1),393K=",difft1_imc)
difft1_bct=arrdiff(d0bct,Qabct,R,T1)
print("Dbct(m^2s^-1),393K=",difft1_bct)
################T2#########################################
difft2_fcc=arrdiff(d0fcc,Qafcc,R,T2)
print("Dfcc(m^2s^-1),423K=",difft2_fcc)
difft2_imc=arrdiff(d0imc,Qaimc,R,T2)
print("Dimc(m^2s^-1),423K=",difft2_imc)
difft2_bct=arrdiff(d0bct,Qabct,R,T2)
print("Dbct(m^2s^-1),423K=",difft2_bct)
##############Save them as text file#######################
Diff_mat=np.array([[T1,difft1_fcc,difft1_imc,difft1_bct],[T2,difft2_fcc,difft2_imc,difft2_bct]])
#Diff_mat=Diff_mat.reshape(1,3)
np.savetxt('Diff-phasesT.txt',Diff_mat,delimiter=",",header='T,Dfcc,Dimc,Dbct ',footer='T=... [K], D...[m^2s^-1]')




