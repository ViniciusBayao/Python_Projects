# Método de interpolação polinomial de Lagrange
from scipy.interpolate import lagrange
import numpy as np
from numpy.polynomial.polynomial import Polynomial
x = np.array([2, 3, 4, 5])
y = np.array([1, 4, 2, 6])
poly = lagrange(x, y)
print(Polynomial(poly))
