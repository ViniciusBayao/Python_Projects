# Método da substituição Retroativa (eliminação de Gauss)
import numpy as np

print('Método de substituição retroativa')
print('')
A = ([[2, 3, 0], [1, -2, 0]])  # Matriz dos coeficientes
print('Matriz dos coeficientes')
print(A)
print('-' * 20)
B = ([0, 5, 0], [0, -9, 0])  # Matriz dos termos independentes
print('Matriz dos termos independentes')
print(B)
print('-' * 20)
print(' ')
# C = np.array([[1, 1, 1, 7], [0, 1, -3, -10], [0, 0, -13, -52]])  # Exibir o sistema
# print('Sistema')
# print(C)
print('-' * 20)
print('             Sistema - Método retroativo              ')
x = np.zeros(3)
x[2] = B[2] / A[2][2]
n = 3
for i in np.arange(n - 2, -1, -1):
    SOMA = 0
    print(f'O valor de i: {i}')
    for j in np.arange(i + 1, n):
        SOMA += A[i][j] * x[j]
        print(f'valor de j: {j}')
    x[i] = (B[i] - SOMA) / A[i][i]
    print(x[i])
print('')
print(f'A solução do sistema é: {x}')

# Método de decomposição LU
