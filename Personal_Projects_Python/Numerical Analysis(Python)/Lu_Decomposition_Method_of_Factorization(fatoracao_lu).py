# Método de decomposição da fatoração LU

import numpy as np


def fatora_lu(a):
    """

    Realiza a fatoração LU para a matriz A

    entrada:
    A - matriz; array[i, j]

    saída:
    L, U - matriz triangular inferior e superior; array[i,j]
    """

    u_m = np.copy(a)
    n = np.shape(u_m)[0]  # Dimensão
    l_m = np.eye(n)  # auxiliar
    for j in np.arange(n - 1):
        for i in np.arange(j + 1, n):
            l_m[i, j] = u_m[i, j] / u_m[j, j]
            for k in np.arange(j + 1, n):
                u_m[i, k] = u_m[i, k] - l_m[i, j] * u_m[j, k]
            u_m[i, j] = 0
    return l_m, u_m


print(fatora_lu(([[1, 2, 3], [4, 5, 6], [7, 8, 9]])))
