from numpy import linalg


def metodo_sist_linear():
    quant_pontos = int(input('QUantidade de pontos: '))
    x_pontos, y_pontos = [], []
    print()
    for i in range(quant_pontos):
        ponto_x = float(input(f'x{i} = '))
        ponto_y = float(input(f'y{i} = '))
        x_pontos.append(ponto_x), y_pontos.append(ponto_y)

    x = float(input('\n Valor x a ser estimado: '))
    a, b = [], []
    for i in range(quant_pontos):
        potencia = 0
        grau = quant_pontos - 1
        linha = []
        while potencia <= grau:
            coef = pow(x_pontos[i], potencia)
            linha.append(coef)
            potencia += 1
        b.append(y_pontos[i])
        a.append(linha)

    coefs_polinomio = linalg.solve(a, b)

    for i in range(len(coefs_polinomio)):
        print(f'a{i} = {coefs_polinomio[i]}')

    aprox = 0
    for i in range(len(coefs_polinomio)):
        aprox += coefs_polinomio[i] * pow(x, i)

    print(f'A proximação encontrada foi de: {aprox}')

metodo_sist_linear()
