import math


def f(x):
    return math.exp(x) - 8


e = 0.01
L = 12
x0 = 2
x1 = 3
x2 = x1 - (x1 - x0) * f(x1)/(f(x1) - f(x0))
i = 1
while (abs(f(x2)) > e) and (i <= L):
    x0 = x1
    x1 = x2
    x2 = x1 - (x1 - x0) * f(x1) / (f(x1) - f(x0))
    i += 1
raiz = 0
if i > L:
    print('Não houve convergência!')
if abs(f(x2)) <= e:
    raiz = x2
print(f'O valor da raíz é: {raiz}')
