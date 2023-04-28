

def gauss_seidel(a, b, vetor_soluc, iteracoes):
    iteracao = 0
    while iteracao < iteracoes:
        for i in range(len(a)):
            x = b[i]
            for j in range(len(a)):
                if i != j:
                    x -= a[i][j]*vetor_soluc[j]
            x /= a[i][i]
            vetor_soluc[i] = x
        iteracao += 1
    print(iteracao)
    print(vetor_soluc)


gauss_seidel([[10, -1, 2, 0], [-5, 11, -1, 3], [3, -1, 10, -1], [1, 3, -1, 8]], [6, 25, -11, 15], [1, 1, 1, 1], 12)
