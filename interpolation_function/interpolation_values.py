########################
# Reference data: A. M. Erer et al (2011), EPJ AP vol. 54 (1), pp. 11302.
# theta_1 = theta_0*exp(-beta*x1); theta_2 = theta_0*exp(-beta*x2)
#
########################
import numpy as np
######Contact Angle#######
def thetax(theta0,beta,x):
    exponent_term=np.exp(-beta*x)
    return theta0*exponent_term
######exponential_constant################
def beta(theta1,theta2,x1,x2):
    logarithmic_term=np.log(theta1)-np.log(theta2)
    return logarithmic_term/(x2-x1)
######exponential_constant################
def amplitude(theta1,beta,x1):
    exponent_term=np.exp(-beta*x1)
    return theta1/exponent_term
# numerical data file of phases
filename_phases="contact_angle.txt"
# Load data from tsv file: data
data_phases=np.loadtxt(filename_phases, delimiter=",", skiprows=1, 
                  usecols=[0,1,2,3,4,5])
xlow=data_phases[0]
theta1=data_phases[1]
xhigh=data_phases[2]
theta2=data_phases[3]
xn1=data_phases[4]
xn2=data_phases[5]
########################################
#R=8.31 #J/molK
#T1=393.15 #K 120 oC
#T2=423.15 #K 150 oC
#####Compute diffusivity of the phases####################
###########Print the diffusivities###############3
################T1#########################################
#########Calculate Beta####################################
beta_constant=beta(theta1,theta2,xlow,xhigh)
print("Beta is=",beta_constant)
#########Calculate Amplitude####################################
theta_0=amplitude(theta1,beta_constant,xlow)
print("Amplitude=",theta_0)
#########Calculate Interpolated contact angles at wt% x####################################
theta_low=thetax(theta_0,beta_constant,xlow)
print("Validation theta_low=",theta_low)
theta_n1=thetax(theta_0,beta_constant,xn1)
print("xn1, theta at x->n1=",xn1,theta_n1,sep='   ')
theta_n2=thetax(theta_0,beta_constant,xn2)
print("xn2, theta at x->n2=",xn2, theta_n2,sep='   ')
theta_high=thetax(theta_0,beta_constant,xhigh)
print("Validation theta_high=",theta_high)

xtheta_mat=np.array([[xlow,theta_low],[xn1,theta_n1],[xn2,theta_n2],[xhigh,theta_high]])
#Diff_mat=Diff_mat.reshape(1,3)
np.savetxt('xsthetas.txt',xtheta_mat,delimiter=",",header='x, theta ',footer='amplitude and beta are printed in terminal')

