def aumentar(n=0, pctg=0, form=False):
    if form is False:
        aumenta = n + (pctg/100 * n)
        return aumenta
    else:
        aumenta = n + (pctg / 100 * n)
        return f'{aumenta:.2f}'


def diminuir(n=0, pctg=0, form=False):
    if form is False:
        diminui = n - (pctg/100 * n)
        return diminui
    else:
        diminui = n - (pctg / 100 * n)
        return f'{diminui:.2f}'


def dobro(n=0, form=False):
    if form is False:
        return n * 2
    else:
        return f'{n * 2:.2f}'


def metade(n=0, form=False):
    if form is False:
        return n / 2
    else:
        return f'{n / 2 :.2f}'


def moeda(preço=0, moeda='R$'):
        return f'{moeda}{preço:>.2f}'.replace('.',',')




