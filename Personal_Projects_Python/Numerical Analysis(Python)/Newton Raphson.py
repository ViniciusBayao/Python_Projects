from sympy import *
from math import *
import sympy as smp

e = smp.symbols('e')
x0 = smp.symbols('x0')


def funcao(x0):
    return exp(x0) - 8


def derivada(x0):
    return smp.diff(exp(x0) - 8)


raiz = 0


def nr(x0, tol, n):

    x1 = x0 - funcao(x0)/derivada(x0)

    i = 1

    while (abs(funcao(x1)) > tol) and (i <= n):

        x0 = x1

        x1 = x0 - funcao(x0)/derivada(x0)

        i = i+1

    if i > n:

        print('Nao houve convergencia!')

    if abs(funcao(x1)) < tol:

        return x1, raiz


print(nr(3, 0.01, 5))
