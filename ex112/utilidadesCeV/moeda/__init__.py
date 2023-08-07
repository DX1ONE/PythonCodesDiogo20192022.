def aumentar(n=0, pctg=0, form=False):
    """
    ->Aumenta o valor de um preço retornando com ou sem formatação.
    :param n:Preço para ser aumentado.
    :param pctg:Em quantos por cento quer que o preço aumente.
    :param form:True para mostrar a formatação, False para não mostrar.
    :return:O preço  acrescido da porcentagem escritos, com ou sem formatação.
    """
    aumenta = n + (pctg/100 * n)
    return aumenta if form is False else moeda(aumenta)


def diminuir(n=0, pctg=0, form=False):
    """
    ->Diminui o valor de um preço retornando com ou sem formatação.
    :param n:Preço para ser reduzido.
    :param pctg:Em quantos por cento quer que o preço reduza.
    :param form:True para mostrar a formatação, False para não mostrar.
    :return:O preço acrescido da porcentagem escritos, com ou sem formatação.
    """
    diminui = n - (pctg/100 * n)
    return diminui if form is False else moeda(diminui)


def dobro(n=0, form=False):
    """
    ->Dobra o valor de um preço retornando com ou sem formatação.
    :param n: Preço para ser dobrado.
    :param form: True para mostrar a formatação, False para não mostrar.
    :return: O preço digitado dobrado, com ou sem formatação.
    """
    dobra = n * 2
    return dobra if form is False else moeda(dobra)


def metade(n=0, form=False):
    """
    ->Reduz o valor de um preço pela metade, retornando com ou sem formatação.
    :param n: Preço para ser reduzido pela metade.
    :param form: True para mostrar a formatação, False para não mostrar.
    :return: O preço digitado pela metade, com ou sem formatação.
    """
    corta = n / 2
    return corta if form is False else moeda(corta)


def moeda(preço=0, moeda='R$'):
    """
    ->Formata o preço digitado com a moeda de desejo, sem câmbio entre as moedas.
    :param preço: O preço para ser formatado.
    :param moeda: A moeda desejada para o preço.
    :return: O preço formatado em forma da moeda digitada.
    """
    return f'{moeda}{preço:>.2f}'.replace('.',',')


def resumo(p, aum=10, red=10):
    """
    ->Cria um resumo organizado com várias análises do preço digitado, captando ainda as porcentagens para tratar o valor.
    :param p: O preço para ser tratado.
    :param aum: A porcentagem desejada para acrescer ao valor digitado.
    :param red: A porcentagem desejada para reduzir do valor digitado.
    :return: Um resumo com vários tratamentos do preço digitado e as porcentagens.
    """
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
