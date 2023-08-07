def notas(*n, sit=False):
    """
    ->Função para captar as notas e analisar a situação de um grupo acadêmico.
    :param n: Uma ou mais nota(s) do(s) aluno(s) -- (Aceita várias)
    :param sit:Mostra a situação do grupo -- (Opcional)
    :return:Um dicionário com várias informações sobre a situação do grupo.
    """
    media = 0
    boletim = dict()
    boletim['Total'] = len(n)
    boletim['Maior'] = max(n)
    boletim['Menor'] = min(n)
    boletim['Média'] = sum(n)/len(n)
    if sit is True:
        if boletim['Média'] < 5:
            sit = 'Ruim'
        elif boletim['Média'] < 7:
            sit = 'Razoável'
        else:
            sit = 'Boa'
        boletim['Situação'] = sit
    return boletim


# Programa Principal
resp = notas(5.5, 9.5, 10, 6.5, sit=True)
print(resp)
help(notas)