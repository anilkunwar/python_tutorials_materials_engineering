#https://stackoverflow.com/questions/48362180/find-common-tangent-line-between-two-cubic-curves
import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
import sys
from sympy import *
import sympy as sym
import os
import pickle as pl


# Intial candidates for fit, per FU: - thus, the E vs V input data has to be per FU
E0_init = -941.510817926696  # -1882.50963222/2.0 
V0_init = 63.54960592453 #125.8532/2.0 
B0_init = 76.3746233515232 #74.49 
B0_prime_init = 4.05340727164527 #4.15

def BM(x, a, b, c, d):
         return  a + b*x + c*x**2 + d*x**3 

def devBM(x, b, c, d):
         return  b + 2*c*x + 3*d*x**2 

# Data 1 (Red triangles): 
V_C_I, E_C_I = np.loadtxt('./1.dat', skiprows = 1).T

# Data 14 (Empty grey triangles):
V_14, E_14 = np.loadtxt('./2.dat', skiprows = 1).T

init_vals = [E0_init, V0_init, B0_init, B0_prime_init]
popt_C_I, pcov_C_I = curve_fit(BM, V_C_I, E_C_I, p0=init_vals)
popt_14, pcov_14 = curve_fit(BM, V_14, E_14, p0=init_vals)


def equations(p):
    x1, x2 = p
    E1 = devBM(x1, popt_C_I[1], popt_C_I[2], popt_C_I[3]) - devBM(x2, popt_14[1], popt_14[2], popt_14[3])
    E2 = ((BM(x1, popt_C_I[0], popt_C_I[1], popt_C_I[2], popt_C_I[3]) - BM(x2, popt_14[0], popt_14[1], popt_14[2], popt_14[3])) / (x1 - x2)) - devBM(x1, popt_C_I[1], popt_C_I[2], popt_C_I[3])
    return (E1, E2)

from scipy.optimize import least_squares
lb = (61.0, 59.0)   # lower bounds on x1, x2
ub = (62.0, 60.0)   # upper bounds
result = least_squares(equations, [61, 59], bounds=(lb, ub))
result_tight_tols = least_squares(equations, [61, 59], ftol=1e-12, xtol=1e-12, gtol=1e-12, bounds=(lb, ub))

print """
####  ftol=1e-08, xtol=1e-08, gtol=1e-08  #####
"""
print 'result = ', result
print 'result.x = ', result.x
print """
something
"""
x1 = result.x[0]
x2 = result.x[1]

slope_common_tangent = devBM(x1, popt_C_I[1], popt_C_I[2], popt_C_I[3])
print 'slope_common_tangent = ', slope_common_tangent

def comm_tangent(x, x1, slope_common_tangent):
   return BM(x1, popt_C_I[0], popt_C_I[1], popt_C_I[2], popt_C_I[3]) - slope_common_tangent * x1 + slope_common_tangent * x

# Linspace for plotting the fitting curves:
V_C_I_lin = np.linspace(V_C_I[0]-2, V_C_I[-1], 10000)
V_14_lin = np.linspace(V_14[0], V_14[-1]+2, 10000)


plt.figure()

# Plotting the fitting curves:
p2, = plt.plot(V_C_I_lin, BM(V_C_I_lin, *popt_C_I), color='black' )
p6, = plt.plot(V_14_lin, BM(V_14_lin, *popt_14), 'b' )

xp = np.linspace(54, 68, 100)
pcomm_tangent, = plt.plot(xp, comm_tangent(xp, x1, slope_common_tangent), 'green', label='Common tangent')

# Plotting the scattered points: 
p1 = plt.scatter(V_C_I, E_C_I, color='red', marker="^", label='1', s=100)
p5 = plt.scatter(V_14, E_14, color='grey', marker="^", facecolors='none', label='2', s=100)

fontP = FontProperties()
fontP.set_size('13')

plt.legend((p1, p2, p5, p6, pcomm_tangent), ("1", "Cubic fit 1", "2", 'Cubic fit 2', 'Common tangent'), prop=fontP)
plt.title('Least squares. Default tolerances: ftol=1e-08, xtol=1e-08, gtol=1e-08')

plt.ticklabel_format(useOffset=False)

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

slope_common_tangent = devBM(x1, popt_C_I[1], popt_C_I[2], popt_C_I[3])
print 'slope_common_tangent = ', slope_common_tangent

def comm_tangent(x, x1, slope_common_tangent):
   return BM(x1, popt_C_I[0], popt_C_I[1], popt_C_I[2], popt_C_I[3]) - slope_common_tangent * x1 + slope_common_tangent * x

# Linspace for plotting the fitting curves:
V_C_I_lin = np.linspace(V_C_I[0]-2, V_C_I[-1], 10000)
V_14_lin = np.linspace(V_14[0], V_14[-1]+2, 10000)


plt.figure()

# Plotting the fitting curves:
p2, = plt.plot(V_C_I_lin, BM(V_C_I_lin, *popt_C_I), color='black' )
p6, = plt.plot(V_14_lin, BM(V_14_lin, *popt_14), 'b' )

xp = np.linspace(54, 68, 100)
pcomm_tangent, = plt.plot(xp, comm_tangent(xp, x1, slope_common_tangent), 'green', label='Common tangent')

# Plotting the scattered points: 
p1 = plt.scatter(V_C_I, E_C_I, color='red', marker="^", label='1', s=100)
p5 = plt.scatter(V_14, E_14, color='grey', marker="^", facecolors='none', label='2', s=100)

fontP = FontProperties()
fontP.set_size('13')

plt.legend((p1, p2, p5, p6, pcomm_tangent), ("1", "Cubic fit 1", "2", 'Cubic fit 2', 'Common tangent'), prop=fontP)
plt.title('ftol=1e-08, xtol=1e-08, gtol=1e-08')

plt.ticklabel_format(useOffset=False)

plt.title('Lest Squares. Tightening tolerances: ftol=1e-12, xtol=1e-12, gtol=1e-12')

print """
#### Using `fsolve`, but restricting the region:  ####

"""

from scipy.optimize import fsolve
x1, x2 =  fsolve(equations, (61.5, 62))

print 'x1 = ', x1
print 'x2 = ', x2

slope_common_tangent = devBM(x1, popt_C_I[1], popt_C_I[2], popt_C_I[3])
print 'slope_common_tangent = ', slope_common_tangent

plt.figure()

# Plotting the fitting curves:
p2, = plt.plot(V_C_I_lin, BM(V_C_I_lin, *popt_C_I), color='black' )
p6, = plt.plot(V_14_lin, BM(V_14_lin, *popt_14), 'b' )

xp = np.linspace(54, 68, 100)
pcomm_tangent, = plt.plot(xp, comm_tangent(xp, x1, slope_common_tangent), 'green', label='Common tangent')

# Plotting the scattered points: 
p1 = plt.scatter(V_C_I, E_C_I, color='red', marker="^", label='1', s=100)
p5 = plt.scatter(V_14, E_14, color='grey', marker="^", facecolors='none', label='2', s=100)

fontP = FontProperties()
fontP.set_size('13')

plt.legend((p1, p2, p5, p6, pcomm_tangent), ("1", "Cubic fit 1", "2", 'Cubic fit 2', 'Common tangent'), prop=fontP)
plt.ticklabel_format(useOffset=False)

plt.title('Using `fsolve`, but restricting the region')



plt.show()
