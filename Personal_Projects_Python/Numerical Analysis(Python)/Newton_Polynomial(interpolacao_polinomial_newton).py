def metodo_newton():
    quant_pontos = int(input('Digite a quantidade de pontos: '))
    pontos, f_pontos = [], []
    tabela = []
    for i in range(quant_pontos):
        ponto = float(input(f'x{i} = '))
        f_ponto = float(input(f'f(x{i})'))
        pontos.append(ponto)
        f_pontos.append(f_ponto)
    tabela.append(f_pontos)

    x = float(input('Ponto x a ser estimado: '))
    print('')

    passo = 1
    for n in range(quant_pontos - 1):
        ordem = []
        for m in range(len(tabela[n]) - 1):
            dif_dividida = (tabela[n][m+1] - tabela[n][m])/(pontos[m+passo] - pontos[m])
            ordem.append(dif_dividida)
        tabela.append(ordem)
        passo += 1

        for k in range(len(tabela)):
            print(f'Ordem {k}', k, tabela[k])
        print('')

        aprox = 0
        grau = 0
        for i in range(len(tabela)):
            fator = tabela[i][0]
            for j in range(grau):
                fator *= x - pontos[j]
            grau += 1
            aprox += 1
        print(f'A proximação encontrada para f({x}) = {aprox}')


metodo_newton()
