# This code finds common tangent for two curves having quadratic fitting
#https://stackoverflow.com/questions/48362180/find-common-tangent-line-between-two-cubic-curves
# Python code to produce common tangent between two curves using least square optimization
# (a) default tolerance, (b) tighter tolerance, and (c) fsolve function
import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
import sys
from sympy import *
import sympy as sym
import os
import pickle as pl

#The slope of a common tanget is defined as following:
# Let G be Gibbs free energy (J/mol) and x_i is the mole fraction of Sn.
# slope = (Gcu(x1)-Gsn(x2))/x1-x2 = mu_sn(x1)=mu_cu(x2)
# Thus we have two equations with two unknowns x1=xeq_sn/cu, and x2=xeq_cu/sn
# Intial candidates for fit, per FU: - thus, the E vs V input data has to be per FU
#G0_init = -2.88188E+04  # J/mol -1882.50963222/2.0 
#M0_init = 7.27463E-01  #125.8532/2.0 mole fraction of Sn for Cu phase
#B0_init = 9.99750E-02 #74.49 
A0_init = 46428.5  # J/mol -1882.50963222/2.0 
B0_init = -14897.3  #125.8532/2.0 mole fraction of Sn for Cu phase
C0_init = -2.88188E+04 #74.49 
#D0CU_init = 0.5
#D0SN_init = 0.8
#B0_prime_init = 2.50000E-04 #4.15

#Function for free energy of phase in parabolic fitting
def freeEnergy(x, a, b, c):
         return   a*x**2 + b*x + c

# Chemical potential function as derivative of freeEnergy function
def chemPot(x, a, b):
         return    2*a*x + b

# Data 1 (Red triangles): 
M_cu, G_cu = np.loadtxt('./cu.dat', skiprows = 1).T

# Data 14 (Empty grey triangles):
M_sn, G_sn = np.loadtxt('./sn.dat', skiprows = 1).T

#init_vals = [G0_init, M0_init, B0_init, B0_prime_init]
init_vals = [A0_init, B0_init, C0_init]
#init_vals_sn = [A0_init, B0_init, C0_init, D0SN_init]
popt_cu, pcov_cu = curve_fit(freeEnergy, M_cu, G_cu, p0=init_vals)
popt_sn, pcov_sn = curve_fit(freeEnergy, M_sn, G_sn, p0=init_vals)

# Define the equations now
# E1: fprime(x1)=gprime(x2)
# E2: f(x1)-g(x2)/(x1-x2) - fprime(x1)
def equations(p):
    x1, x2 = p
    E1 = chemPot(x1, popt_cu[1], popt_cu[2]) - chemPot(x2, popt_sn[1], popt_sn[2] )
    E2 = ((freeEnergy(x1, popt_cu[0], popt_cu[1], popt_cu[2]) - freeEnergy(x2, popt_sn[0], popt_sn[1], popt_sn[2])) / (x1 - x2)) - chemPot(x1, popt_cu[1], popt_cu[2])
    return (E1, E2)

####LEAST_SQUARE_OPTIMIZATION_METHODS (LSOM)
from scipy.optimize import least_squares
lb = (0.70, 0.91)   # lower bounds on x1, x2
ub = (0.75, 0.95)   # upper bounds
result = least_squares(equations, [0.70, 0.91], bounds=(lb, ub))
result_tight_tols = least_squares(equations, [0.70, 0.91], ftol=1e-12, xtol=1e-12, gtol=1e-12, bounds=(lb, ub))

#LSOM METHOD-I (DEFAULT_TOLERANCES)
print """
####  ftol=1e-08, xtol=1e-08, gtol=1e-08  #####
"""
print 'result = ', result
print 'result.x = ', result.x
print """
####something
"""
x1 = result.x[0]
x2 = result.x[1]

slope_common_tangent = chemPot(x1, popt_cu[1], popt_cu[2])
print 'slope_common_tangent = ', slope_common_tangent

def comm_tangent(x, x1, slope_common_tangent):
   return freeEnergy(x1, popt_cu[0], popt_cu[1], popt_cu[2]) - slope_common_tangent * x1 + slope_common_tangent * x

# Linspace for plotting the fitting curves:
M_cu_lin = np.linspace(M_cu[0]-2, M_cu[-1], 10000)
M_sn_lin = np.linspace(M_sn[0], M_sn[-1]+2, 10000)


plt.figure()

# Plotting the fitting curves:
p2, = plt.plot(M_cu_lin, freeEnergy(M_cu_lin, *popt_cu), color='black' )
p6, = plt.plot(M_sn_lin, freeEnergy(M_sn_lin, *popt_sn), 'b' )

xp = np.linspace(0.70, 0.80, 1.0)
pcomm_tangent, = plt.plot(xp, comm_tangent(xp, x1, slope_common_tangent), 'green', label='Common tangent')

# Plotting the scattered points: 
p1 = plt.scatter(M_cu, G_cu, color='red', marker="^", label='1', s=100)
p5 = plt.scatter(M_sn, G_sn, color='grey', marker="^", facecolors='none', label='2', s=100)

fontP = FontProperties()
fontP.set_size('13')

plt.legend((p1, p2, p5, p6, pcomm_tangent), ("1", "Quadratic fit 1", "2", 'Quadratic fit 2', 'Common tangent'), prop=fontP)
plt.title('Least squares. Default tolerances: ftol=1e-08, xtol=1e-08, gtol=1e-08')

plt.ticklabel_format(useOffset=False)

#LSOM METHOD-II (FINE_TOLERANCES)
### Tighter tolerances:
print """
####  ftol=1e-12, xtol=1e-12, gtol=1e-12  #####
"""
print 'result_tight_tols = ', result_tight_tols
print 'result_tight_tols.x = ', result_tight_tols.x
print """

"""
x1 = result_tight_tols.x[0]
x2 = result_tight_tols.x[1]

slope_common_tangent = chemPot(x1, popt_cu[1], popt_cu[2])
print 'slope_common_tangent = ', slope_common_tangent

def comm_tangent(x, x1, slope_common_tangent):
   return freeEnergy(x1, popt_cu[0], popt_cu[1], popt_cu[2]) - slope_common_tangent * x1 + slope_common_tangent * x

# Linspace for plotting the fitting curves:
M_cu_lin = np.linspace(M_cu[0]-2, M_cu[-1], 10000)
M_sn_lin = np.linspace(M_sn[0], M_sn[-1]+2, 10000)


plt.figure()

# Plotting the fitting curves:
p2, = plt.plot(M_cu_lin, freeEnergy(M_cu_lin, *popt_cu), color='black' )
p6, = plt.plot(M_cu_lin, freeEnergy(M_sn_lin, *popt_sn), 'b' )

xp = np.linspace(0.70, 0.80, 1.0)
pcomm_tangent, = plt.plot(xp, comm_tangent(xp, x1, slope_common_tangent), 'green', label='Common tangent')

# Plotting the scattered points: 
p1 = plt.scatter(M_cu, G_cu, color='red', marker="^", label='1', s=100)
p5 = plt.scatter(M_sn, G_sn, color='grey', marker="^", facecolors='none', label='2', s=100)

fontP = FontProperties()
fontP.set_size('13')

plt.legend((p1, p2, p5, p6, pcomm_tangent), ("1", "Quadratic fit 1", "2", 'Quadratic fit 2', 'Common tangent'), prop=fontP)
#plt.title('ftol=1e-08, xtol=1e-08, gtol=1e-08')

plt.ticklabel_format(useOffset=False)

plt.title('Least Squares. Tightening tolerances: ftol=1e-12, xtol=1e-12, gtol=1e-12')

#####FSOLVE METHOD of SCIPY OPTIMIZATION (METHOD III)
print """
#### Using `fsolve`, but restricting the region:  ####

"""

from scipy.optimize import fsolve
x1, x2 =  fsolve(equations, (0.80, 0.90))

print 'x1 = ', x1
print 'x2 = ', x2

slope_common_tangent = chemPot(x1, popt_cu[1], popt_cu[2]) #chemPot = d(freeEnergy)/d(x_sn)
print 'slope_common_tangent = ', slope_common_tangent

plt.figure()

# Plotting the fitting curves:
p2, = plt.plot(M_cu_lin, freeEnergy(M_cu_lin, *popt_cu), color='black' )
p6, = plt.plot(M_sn_lin, freeEnergy(M_sn_lin, *popt_sn), 'b' )

xp = np.linspace(0.70, 0.80, 1.0)
pcomm_tangent, = plt.plot(xp, comm_tangent(xp, x1, slope_common_tangent), 'green', label='Common tangent')

# Plotting the scattered points: 
p1 = plt.scatter(M_cu, G_cu, color='red', marker="^", label='1', s=100)
p5 = plt.scatter(M_sn, G_sn, color='grey', marker="^", facecolors='none', label='2', s=100)

fontP = FontProperties()
fontP.set_size('13')

plt.legend((p1, p2, p5, p6, pcomm_tangent), ("1", "Quadratic fit 1", "2", 'Quadratic fit 2', 'Common tangent'), prop=fontP)
plt.ticklabel_format(useOffset=False)

plt.title('Using `fsolve`, but restricting the region')



plt.show()
