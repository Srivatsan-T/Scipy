"""
from scipy import constants
print(constants.yotta)
print(constants.kilo)
print(constants.lb)
print(constants.kilo)
"""

"""
from scipy import constants
print(constants.arcmin)
print(constants.arcsec)
print(constants.minute)
print(constants.hour)
print(constants.hectare)
print(constants.gallon_US)
"""

"""
from scipy import constants
print(constants.speed_of_light)
print(constants.speed_of_sound)
print(constants.degree_Fahrenheit)
print(constants.zero_Celsius)
print(constants.eV)
print(constants.light_year)
print(constants.horsepower)
"""

"""
from scipy.optimize import minimize

def eq(x):
    return x**2+x+2

print(minimize(eq,0,method = 'BFGS').x)
"""

from scipy.sparse import csr_matrix
import numpy as np
a = np.array([0,1,2,0,0,0,1])
print(csr_matrix(a))
print(csr_matrix(a).data)
print(csr_matrix(a).count_nonzero())

