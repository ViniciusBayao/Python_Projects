"""
# Método de integração numérica (cálculo da integral) -> Método dos Retângulos:
import numpy as np
import math
f = eval('math.exp(x) / 1 + math.sin(x)')
a, b, N = 1, 2, 20
x = np.linspace(a, b, N+1)
y = f(x)
dx = (b-a)/N
x_medio = np.linspace(dx/2, b - dx/2, N)
soma_retangulo = np.sum(f(x_medio) * dx)
print(f'Integral: {soma_retangulo}')

"""

# Método de integração numérica (cálculo da integral) -> Método dos trapézios:

import math


def metodo_trapezios(func, inter_init, inter_fim, numero):
    h = (inter_fim - inter_init) / numero
    soma = 0
    for k in range(numero):
        soma += func(inter_init + k * h)
    soma *= 2
    soma += (func(inter_init) + func(inter_fim))
    return (h / 2) * soma


def f(x):
    return math.sqrt((math.sin(x)**3) + 1)


a, b = 0, 1
n = 3
integral = metodo_trapezios(f, a, b, n)

print(f'Integral: {integral}')

"""
# Método da integração numérica (calculo da integral) -> Método Simpson
import math


def metodo_simps(func, inter_init, inter_end, number):
    if number % 2 != 0 and number < 1:
        raise ValueError('n deve ser par e maior que 1.')
    h = (inter_end - inter_init) / number
    soma_odd, soma_pair = 0, 0
    for k in range(1, number, 2):
        soma_odd += func(inter_init + k * h)
    for k in range(2, number, 2):
        soma_pair += func(inter_init + k * h)
    return (h / 3) * (func(inter_init) + 4 * soma_odd + 2 * soma_pair + f(inter_end))


def f(x):
    return x ** 3


a, b = 1, 2
n = 20

integral = metodo_simps(f, a, b, n)
print(f'Integral: {integral}')
"""
