# Calculando noção de limite derivada e integral de uma função f(x) em Python
from sympy import *

x, y, z = symbols('x y z')  # Delcaramos as letras que queremos que o programa entenda como símbolos ao invés de variav.

init_printing(use_unicode=True)  # Mostrar a equação final gerada da forma experada na metemática.

print(diff(5*x**3+cos(x), x))  # Exemplo da derivada de uma função qualquer

print(integrate(5*x**3+cos(x), x))  # Exemplo da integral de uma função qualquer

print(limit(5*x**3+cos(x), x, 0))  # Achando o limite de uma função qualquer baseado no x quando tem proximidade a 0.

# f(x) = e**x + 8
# OBS: Quando temos que usar a derivada com termo e de Euler no exponencial na matemática em Python
'''
import sympy as smp

e = smp.Symbol('e')
x = smp.Symbol('x')
f = e**x + 8
print(smp.diff(8 + smp.exp(x)))
'''