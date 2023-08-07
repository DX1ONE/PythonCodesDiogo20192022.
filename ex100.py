from random import randint
from time import sleep
números = []


def sorteia():
    for c in range(0, 5):
        números.append(randint(0, 10))
    print('Sorteando 5 valores da lista: ', end='')
    for n in números:
        print(f'{n}', end=' ')
        sleep(0.5)
    print('-> Pronto!')


def somaPAR():

    pares = []
    soma = 0
    for n in números:
        if n % 2 == 0:
            pares.append(n)
    for contagem, num in enumerate(pares):
        if contagem == 0:
            soma = num
        else:
            soma += num
    if soma >= 2:
        print(f'A soma dos números pares sorteados vale {soma}.')
    else:
        print('A soma dos números pares sorteados vale 0.')


# Programa Principal
sorteia()
somaPAR()
