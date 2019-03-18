# For python3.6
# For analysing the thermodynamics and kinetics of materials at several length and time scales (multiscales),
# it is important to numerically measure the relative magnitude of several physical parameters at different length scales,
# energy scales and time scales
# Outputs the magnitudes of functions at given values of length, energy and time scales
# the relative magnitudes of ls , es, ts, f_chem, M, kappa, and mu.
# Reference website for python commands on strings variables
# https://pythonprogramming.net/python-tutorial-print-function-strings/
# https://en.wikibooks.org/wiki/Python_Programming/Basic_Math
# https://stackoverflow.com/questions/9685946/math-operations-from-string
# http://interactivepython.org/runestone/static/CS152f17/Strings/OperationsonStrings.html
# https://www.learnpython.org/en/Basic_String_Operations
##########################################################################################
ls=float(input("Enter the length scale of the simulation (1E+6 for 1 um, 1.0E-3 for km):   "))
length_scale=ls
ls_name=input("name of the length scale (e.g. nm for nanometer): ")
ls_unit_value=ls_name
es=float(input("Enter the energy scale (6.24E+18 for JtoeV,1.0E+6 for 1 uJ,1.0E-06 for MJ):   "))
energy_scale=es
es_name=input("name of the energy scale (e.g. ev for Electron Volts): ")
es_unit_value=es_name
ts=float(input("Enter the time scale (1 for 1 s, 1000 for 1 ms):   "))
time_scale=ts
ts_name=input("name of the time scale (e.g. s for second): ")
ts_unit_value=ts_name
print("Enter the original magnitudes of physical parameters in SI units")
kappa_input=float(input("Enter kappa (J/m):   "))
kappa=kappa_input
mu_input=float(input("Enter mu (J/m^3):   "))
mu=mu_input
fchem_input=float(input("Enter bulk free energy density (J/m^3):   "))
fchem=fchem_input
ch_mobility_input=float(input("Enter the Cahn-Hilliard mobility in m2*mol/(J s):   "))
ch_mobility=ch_mobility_input
ac_mobility_input=float(input("Enter the Allen-Cahn or Ginzburg-Landau mobility in m3/(J s): "))
ac_mobility=ac_mobility_input
print("scaled outputs are as follow")
kappa_scaled=(es/ls)*kappa
print("scaled kappa is : ")
print(kappa_scaled, es_unit_value+"/"+ls_unit_value )
#print(es_unit_value+"/"+ls_unit_value)
######################################
mu_scaled=(es/ls**3)*mu
print("scaled mu is : ")
print(mu_scaled, es_unit_value + "/"+ ls_unit_value + "**3" )
#######################################
fchem_scaled=(es/ls**3)*fchem
print("scaled bulk free energy density is : ")
print(fchem_scaled, es_unit_value + "/"+ ls_unit_value + "**3" )
#######################################
ch_mobility_scaled=(ls**2/(es*ts))*ch_mobility
print("scaled Cahn-Hilliard Mobility is : ")
print(ch_mobility_scaled, "mol*"+ls_unit_value + "**2" + "/" + "(" + es_unit_value + "*"+ts_unit_value+")" )
#######################################
ac_mobility_scaled=(ls**3/(es*ts))*ac_mobility
print("scaled GL or AC mobility is : ")
print(ac_mobility_scaled, ls_unit_value + "**3" + "/" + "("+es_unit_value+"*"+ts_unit_value+")" )
#####################This coding can be improved by usin list, arrays, tuples and dictionaries
#####################Eureka####################################################################






