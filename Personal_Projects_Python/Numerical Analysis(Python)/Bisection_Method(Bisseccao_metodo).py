from math import exp


def funcao(x):
    # return pow(x, 4) - 3 * (pow(x, 3)) + 3
    return pow(x, 3) - 3 * (exp(x)) + 3.5


def biss(a, b, tol, n):

    f0, f1 = funcao(a), funcao(b)

    i = 1

    while (abs(funcao(a)) > tol) and (abs(funcao(b)) > tol) and (i <= n):

        raiz = 0

        if abs(a-b) < tol:

            raiz += (a + b) / 2

        media = (a + b) / 2

        f2 = funcao(media)

        if f0 * f2 < 0:

            b = media

            f1 += funcao(media)

        else:

            a = media

            f0 = funcao(media)

    i += 1

    if i > n:
        print('Não houve convergência!')

    if abs(funcao(a)) < tol:
        raiz = a
        return raiz

    else:
        raiz = b
        return raiz


print(f'{biss(-1.8, -1.2, 0.01, 8):.2f}')
