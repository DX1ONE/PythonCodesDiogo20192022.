jogador = {}
gols = []
jogador['Nome'] = str(input('Nome do jogador: '))
partidas = int(input(f'Quantas partidas {jogador["Nome"]} jogou?'))
for n in range(0, partidas):
    gols.append(int(input(f'Quantos gols na partida {n}? ')))
    goal = 0
    for cont, g in enumerate(gols):
        if cont == 0:
            goal = g
        else:
            goal += g
jogador['gols'] = gols
jogador['total'] = goal
# poderia somente ter feito (jogador['total'] = sum(gols)), sum - somaria os valores da lista...
print('—' * 50)
print(jogador)
print('—' * 50)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('—' * 50)
print(f'O jogador {jogador["Nome"]} jogou {partidas} partidas.')
for cont, n in enumerate(gols):
    print(f'    =>Na partida {cont}, fez {n} gols.')
print(f'Foi um total de {jogador["total"]} gols.')
