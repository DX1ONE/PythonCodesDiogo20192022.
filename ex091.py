from random import randint
from time import sleep
jogos = {}
lista = []
ordem = []
for j in range(1, 5):
    jogos[f'jogador {j}'] = randint(1, 6)
    lista.append([f'jogador {j}'], )
    lista.append(jogos[f'jogador {j}'])
for k, v in jogos.items():
    print(f'O {k} tirou {v}')
    sleep(0.5)
print('Ranking dos jogadores: ')
for p in range(1, len(jogos) + 1):
    print(f'{p}° lugar: ', end='')
    for c, elem in enumerate(lista):
        if c % 2 != 0:
            ordem.append(elem)
            ordem.sort()
    for e in ordem:
        print(f'{ordem}')
print(lista)

