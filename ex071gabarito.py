from time import sleep
print('\033[1m—\033[m' * 50)
print('\033[1;30;47m{:^50}\033[m'.format('ATM'))
print('\033[1m—\033[m' * 50)
valor = int(input('\033[1mQue valor você quer sacar? R$\033[m'))
print('\033[1mProcessando...\033[m')
sleep(2)
print('\033[1m—\033[m' * 50)
ced = 50
totced = 0
while True:
    if valor >= ced:
        valor -= ced
        totced += 1
    else:
        if totced > 0:
            print(f'\033[1m Cédulas de R${ced}: {totced}\033[m')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totced = 0
        if valor == 0:
            break
print('\033[1m—\033[m' * 50)
print('\033[1;30;47m{:^50}\033[m'.format('Volte Sempre!'))
