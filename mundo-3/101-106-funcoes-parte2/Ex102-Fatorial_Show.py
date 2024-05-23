def fatorial(n, show=False):
    """
    -> Calcula o fatorial de um número.
    :param n: O número a ser calculado.
    :param show: (Opcional) mostrar ou não a conta.
    :return: O valor do fatorial de um número m.
    """
    f = 1
    for c in range(n, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(f' x ', end='')
            else:
                print(' = ', end='')
        f *= c
    return f


num = int(input('Digite um número: '))
print(fatorial(num, show=True))
help(fatorial)