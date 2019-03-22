#! /usr/bin/python
# For python3.6
# Outputs the magnitudes of functions at given values of length, energy and time scales
#References
#https://stackoverflow.com/questions/43971481/covert-error-for-loadtxt-function
#https://stackoverflow.com/questions/23546349/loading-text-file-containing-both-float-and-string-using-numpy-loadtxt
#https://cmdlinetips.com/2018/01/how-to-read-a-numerical-data-file-in-python-with-numpy/
#https://stackoverflow.com/questions/22431921/abbreviate-the-import-of-multiple-files-with-loadtxt-python
#https://scipython.com/book/chapter-6-numpy/examples/using-numpys-loadtxt-method/
##########################################################################################
# import numpy library as np
import numpy as np
temperature_input=float(input("Enter the value of temperature in K (e.g. 313.15 ):   "))
temperature=temperature_input
gas_constant=8.31 #J/mol .K
#Material properties of Aluminum
#Lundy and Murdock 1962, JAP. Vol.33 (5)
#Al_activation=1.4212E+5 #J/mol
#gas_constant=8.31 #J/mol .K
#frequency_factor=1.71E-04 #1.7414E-04 #m^2/s
#diff_al=frequency_factor*np.exp(-Al_activation/(gas_constant*temperature))
def diffusivity(D0,Qa):
    rt=gas_constant*temperature
    return D0*np.exp(-Qa/rt)
#Material properties of Aluminum
#Lundy and Murdock 1962, JAP. Vol.33 (5)
Al_acten=1.4212E+5 #J/mol
Al_d0=1.71E-04 #m^2/s
al_lattice_diff=diffusivity(Al_d0,Al_acten)
#Material properties of Nickel lattice(l) and grain boundary(b)
#Wazzan 1965, JAP. Vol.36 (11)
Nil_qa=2.79224E+5 #J/mol
Nil_d0=1.9E-04 #m^2/s
ni_lattice_diff=diffusivity(Nil_d0,Nil_qa)
Nigb_qa=1.1453199E+5 #J/mol
Nigb_d0=0.07E-04 #m^2/s
ni_gb_diff=diffusivity(Nigb_d0,Nigb_qa)
material_input=input("Type Al_bk or Ni_bk or Ni_gb (_bk = bulk, and _gb=grain boundary): ")
choice=material_input
type(choice) 
#This will help in execution of the last statement "i.e. no material has been defined"
#print(type(choice)) #<type 'str'>
#if ...elif...statements
# https://www.tutorialspoint.com/python/python_if_else.htm
if choice=="Al_bk":
   print("The bulk diffusivity of Al is:")
   print(al_lattice_diff, "m**2/s")
elif choice=="Ni_bk":
   print("The bulk diffusivity of Ni is:")
   print(ni_lattice_diff, "m**2/s")
#else
   #print("The grain boundary diffusivity of Ni is:")
   #print(ni_gb_diff)
elif choice=="Ni_gb":
   print("The grain boundary diffusivity of Ni is:")
   print(ni_gb_diff, "m**2/s")
else:
   print("No material has been defined:")
   #print(ni_gb_diff)

#####################This coding can be improved by usin list, arrays, tuples and dictionaries
#####################Eureka####################################################################
