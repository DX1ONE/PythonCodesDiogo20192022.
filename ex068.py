from random import randint
print('\033[1;32m~\033[m' * 50)
print('\033[1;30;41m{:-^50}\033[m'.format('PAR OU ÍMPAR'))
print('\033[1;32m~\033[m' * 50)
ganhou = 0
while True:
    pc = randint(0, 10)
    escolha = int(input('\033[1;32mDiga um valor: \033[m'))
    soma = escolha + pc
    opcao = str(input('\033[1;32mPar ou ímpar? [P/I]\033[m')).upper().strip()[0]
    while opcao not in 'PI':
        opcao = str(input('\033[1;32mPar ou ímpar? [P/I]\033[m')).upper().strip()[0]
    par = soma % 2
    if par == 0:
        if opcao in 'Pp':
            print(f'\033[1;32mVocê jogou\033[m \033[1;31m{escolha}'
                  f'\033[m \033[1;32me o computador\033[m \033[1;31m{pc}'
                  f'\033[m\033[1;32m.Total de\033[m \033[1;31m{soma}\033[m'
                  f' \033[1;32mdeu\033[m \033[1;31mPAR.\033[m')
            print('\033[1;31m{:-^50}\033[m'.format('YOU WIN!'))
            print('\033[1;32mVamos jogar novamente...\033[m')
            ganhou += 1
        elif opcao in 'Ii':
            print(f'\033[1;32mVocê jogou\033[m \033[1;31m{escolha}'
                  f'\033[m \033[1;32me o computador\033[m \033[1;31m{pc}'
                  f'\033[m\033[1;32m.Total de\033[m \033[1;31m{soma}\033[m'
                  f' \033[1;32mdeu\033[m \033[1;31mPAR.\033[m')
            print('\033[1;30;41m{:-^50}\033[m'.format('GAME OVER!'))
            print('\033[1;32m~\033[m' * 50)
            print(f'\033[1;31m            Vitórias consecutivas: {ganhou}              \033[m')
            print('\033[1;32m~\033[m' * 50)
            break
        else:
            print('\033[1;31mOpção inválida! Tente Novamente.\033[m')
    elif par != 0:
        if opcao in 'Pp':
            print(f'\033[1;32mVocê jogou\033[m \033[1;31m{escolha}'
                  f'\033[m \033[1;32me o computador\033[m \033[1;31m{pc}'
                  f'\033[m\033[1;32m.Total de\033[m \033[1;31m{soma}\033[m'
                  f' \033[1;32mdeu\033[m \033[1;31mÍMPAR.\033[m')
            print('\033[1;30;41m{:-^50}\033[m'.format('GAME OVER!'))
            print('\033[1;32m~\033[m' * 50)
            print(f'\033[1;31m            Vitórias consecutivas: {ganhou}              \033[m')
            print('\033[1;32m~\033[m' * 50)
            break
        elif opcao in 'Ii':
            print(f'\033[1;32mVocê jogou\033[m \033[1;31m{escolha}'
                  f'\033[m \033[1;32me o computador\033[m \033[1;31m{pc}'
                  f'\033[m\033[1;32m.Total de\033[m \033[1;31m{soma}\033[m'
                  f' \033[1;32mdeu\033[m \033[1;31mÍMPAR.\033[m')
            print('\033[1;31m{:-^50}\033[m'.format('YOU WIN!'))
            print('\033[1;32mVamos jogar novamente...\033[m')
            ganhou += 1
        else:
            print('\033[1;31mOpção inválida! Tente Novamente.\033[m')
