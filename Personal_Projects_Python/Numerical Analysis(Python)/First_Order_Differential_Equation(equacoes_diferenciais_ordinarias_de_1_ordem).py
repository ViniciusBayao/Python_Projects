"""
import numpy as np

from numpy import linalg

import matplotlib.pyplot as plt


def f(t, u):

    return 2*u


# tamanho e num. de passos


h = 0.2

N = 6

# cria vetor t e u

t = np.empty(N)

u = np.copy(t)

# C.I.

t[0] = 0

u[0] = 1

# iteracoes

for i in np.arange(N-1):

    t[i+1] = t[i] + h

    u[i+1] = u[i] + h*f(t[i], u[i])

# imprime

for i, tt in enumerate(t):

    print("%1.1f %1.4f" % (t[i], u[i]))
"""

import math


def f(t, y):
    return x*y


y0 = 3
t0 = 0
h = 1/2
t1 = t0 + h
y1 = y0 + h * f(t0, y0)
t2 = t1 + h
y2 = y1 + h * f(t1, y1)
t3 = t2 + h
y3 = y2 + h * f(t2, y2)
t4 = t3 + h
y4 = y3 + h * f(t3, y3)
t5 = t4 + h
y5 = y4 + h * f(t4, y4)
print(y5)
"""
t6 = t5 + h
y6 = y5 + h * f(t5, y5)
t7 = t6 + h
y7 = y6 + h * f(t6, y6)
t8 = t7 + h
y8 = y7 + h * f(t7, y7)
t9 = t8 + h
y9 = y8 + h * f(t8, y8)
t10 = t9 + h
y10 = y9 + h * f(t9, y9)
print(y10)
"""