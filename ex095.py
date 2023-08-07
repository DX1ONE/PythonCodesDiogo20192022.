jogadores = []
jogador = {}
gols = []
dados = []
while True:
    jogador.clear()
    jogador['Nome'] = str(input('Nome do jogador: '))
    partidas = int(input(f'Quantas partidas {jogador["Nome"]} jogou?'))
    for n in range(0, partidas):
        dados.append(int(input(f'Quantos gols na partida {n + 1}? ')))
        goal = 0
        for cont, g in enumerate(dados):
            if cont == 0:
                goal = g
            else:
                goal += g
    gols.append(dados[:])
    for cont, g in enumerate(gols):
        jogador['gols'] = gols[cont]
    dados.clear()
    jogador['total'] = goal
    jogadores.append(jogador.copy())
    print('—' * 50)
    continuar = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if continuar in 'N':
        break
print('cód. ', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print('-' * 50)
for k, v in enumerate(jogadores):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-' * 50)
while True:
    mostrar = int(input('Mostrar dados de qual jogador? '))
    if mostrar < 0:
        break
    if mostrar > len(jogadores) - 1:
                print(f'ERRO! Não existe jogador com código {mostrar}! Tente Novamente!')
    else:
        for cont, n in enumerate(jogadores):
            if mostrar == cont:
                print(f'--LEVANTAMENTO DO JOGADOR {n["Nome"]}: ')
                for contagem, g in enumerate(n["gols"]):
                    print(f'  No jogo {contagem + 1} fez {g} gols.')
print('{:—^50}'.format('VOLTE SEMPRE!'))
