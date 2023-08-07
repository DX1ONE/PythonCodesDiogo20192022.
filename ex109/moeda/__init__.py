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
