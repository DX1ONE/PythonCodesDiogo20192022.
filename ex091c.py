from random import randint
from time import sleep
jogo = {'jogador 1': randint(1, 6),
        'jogador 2': randint(1, 6),
        'jogador 3': randint(1, 6),
        'jogador 4': randint(1, 6)}
ranking = list()
for k, v in jogo.items():
    print(f'{k} tirou {v} no dado.')
    sleep(1)
# Sem a utilização da importação do itemgetter. -> key=lambda item: item[n°]
ranking =sorted(jogo.items(), key=lambda item: item[1], reverse=True)
print('—' * 40)
print('\033[1;33m==== RANKING DOS JOGADORES ====\033[m')
for i, v in enumerate(ranking):
    print(f'\033[1m  O {i + 1}° lugar: {v[0]} com {v[1]}.\033[m')
    sleep(1)
print('\033[1;33m=\033[m' * 31)