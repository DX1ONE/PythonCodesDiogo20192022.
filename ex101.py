def voto(ano):
    """
    ->Mostra o status do usuário em relação ao seu compromisso com o voto eleitoral.
    :param ano: O ano de Nascimento do usuário
    :return: Se o usuário pode, deve ou se é opcional, votar.
    """
    from datetime import datetime
    idade = datetime.now().year - ano
    if idade < 16 :
        return f'Com {idade} anos: NÃO VOTA. '
    elif 18 <= idade < 65 :
        return f'Com {idade} anos: VOTO OBRIGATÓRIO.'
    else:
        return f'Com {idade} anos: VOTO OPCIONAL.'


# Programa Principal
a = int(input('Em que ano você nasceu?'))
print(voto(a))
print('-' * 50)
help(voto)