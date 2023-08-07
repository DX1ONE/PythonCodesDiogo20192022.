def ficha(nome='<Desconhecido>', gols=0):
    """
    ->Mostra uma string formatada dos dados de um jogador informado.
    :param nome:O nome do jogador.
    :param gols:A quantidade inteira de gols realizados pelo jogador.
    :return:Uma string informando quantos gols o jogador fez no campeonato.
    """
    print(f'O jogador {nome} fez {gols} gol(s) no campeonato.')


# Programa Principal
n = str(input('Nome do Jogador: '))
g = str(input('Número de gols: '))
if g.isnumeric():
    g = int(g)
else:
    g = 0
if n.strip() == '':
    ficha(gols=g)
else:
    ficha(n, g)