def aumentar(n=0, pctg=0, form=False):
    aumenta = n + (pctg/100 * n)
    return aumenta if form is False else moeda(aumenta)


def diminuir(n=0, pctg=0, form=False):
    diminui = n - (pctg/100 * n)
    return diminui if form is False else moeda(diminui)


def dobro(n=0, form=False):
    dobra = n * 2
    return dobra if form is False else moeda(dobra)


def metade(n=0, form=False):
    corta = n / 2
    return corta if form is False else moeda(corta)


def moeda(preço=0, moeda='R$'):
    return f'{moeda}{preço:>.2f}'.replace('.',',')


def resumo(p, aum=10, red=10):
    print('—' * 30)
    print('{:^30}'.format('RESUMO DO VALOR'))
    print('—' * 30)
    lista = ('Preço analisado:', f'\t{moeda(p)}', 'Dobro do preço :', f'\t{dobro(p, True)}',
             'Metade do preço:', f'\t{metade(p,True)}', f'{aum}% de aumento :',
             f'\t{aumentar(p, aum, True)}', f'{red}% de redução :', f'\t{diminuir(p, red, True)}')

    for c in range(0, len(lista)):
        if c == 0 or c % 2 == 0:
            print(f'{lista[c]}', end='')
        elif c % 2 != 0:
            print(lista[c])
    print('—' * 30)
