import numpy as np
xi = np.array([2, 3, 4])
yi = np.array([3, 7, 9])
V = np.array([xi**1, xi**0]).transpose()
a = ((np.linalg.inv((V.transpose()).dot(V))).dot(V.transpose())).dot(yi)
print(f'f(x) = {a[1]:.2f} {a[0]:.2f}x')
