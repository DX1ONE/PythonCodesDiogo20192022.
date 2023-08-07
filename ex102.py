def fatorial(num, show=False):
    """
    ⇒Calcula o fatorial de um número.
    :param num:O número a ser calculado
    :param show:(opcional) Mostrar ou não o cálculo.
    :return:O valor do Fatorial de um número n.
    """
    f = 1
    if show is False:
        for c in range(num, 0, -1):
            f *= c
        return f
    else:
        for c in range(num, 0, -1):
            f *= c
            print(f'{num}', end=' ')
            print('x ' if c > 1 else '= ', end='')
            num -= 1
        return f


# Programa Principal
print(fatorial(5))
print(fatorial(5, show=True))
print(fatorial(5, False))
print('-' * 50)
help(fatorial)