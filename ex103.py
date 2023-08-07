def ficha(nome=0, gols=0):
    print(f'O jogador {nome} fez ' if nome is True else f'O jogador <Desconhecido> fez ', end='')
    print(f'{gols} gol(s) no campeonato' if gols is True else f'0 gol(s) no campeonato.')


# Programa Principal
n = str(input('Nome do Jogador: '))
g = str(input('Número de Gols: '))
if g.isnumeric():
    g = int(g)
else:
    g = 0

