import numpy as np


def sigma_calc(mu,delta):
    sigma=[]
    for k in range(len(mu)):
        sigma_value=(mu[k]*delta)/6.0
        sigma.append(sigma_value)
    return sigma


mu=[1.0E+08,2.0E+08,3.0E+08,4.0E+08, 5.0E+08, 6.0E+08, 7.0E+08, 8.0E+08, 9.0E+08, 10.0E+08] #J/m3
delta=1.0E-08 #10 nm
sigma=sigma_calc(mu,delta)

# Reference: http://hplgit.github.io/bumpy/doc/pub/lectures-basics-solarized.html#___sec57
# Make two-dimensional array of [mu, sigma(mu)] values in each row
data = np.array([mu, sigma]).transpose()

# Write data array to file in table format
np.savetxt('mu_sigma.dat', data, fmt=['%.2f', '%.4f'],
           header='mu(J/m3)   sigma(J/m2)', comments='# ')


