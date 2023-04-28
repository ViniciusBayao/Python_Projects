
def gauss_jacob(a, b, vetor_soluc, iteracoes):
    iteracao = 0
    vetor_auxiliar = []
    for k in range(len(vetor_soluc)):
        vetor_auxiliar.append(0)

    while iteracao < iteracoes:
        for i in range(len(a)):
            x = b[i]
            for j in range(len(a)):
                if i != j:
                    x -= a[i][j] * vetor_soluc[j]
            x /= a[i][i]
            vetor_auxiliar[i] = x
        iteracao += 1

        for p in range(len(vetor_auxiliar)):
            vetor_soluc[p] = vetor_auxiliar[p]
    print(vetor_soluc)


gauss_jacob([[4, -2, -1], [-1, 6, 1], [-1, 1, 7]], [3, 9, -6], [0, 0, 0], 10)
