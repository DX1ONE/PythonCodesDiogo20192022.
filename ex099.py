from time import sleep


def maior(*núm):
    m = 0
    for cont, n in enumerate(núm):
        if cont == 0:
            m = n
        else:
            if n > m:
                m = n
    print('-=' * 20)
    print('Analisando os valores passados.', end='')
    sleep(0.5)
    print('.', end='')
    sleep(0.5)
    print('.')
    sleep(1)
    for n in núm:
        print(f'{n}', end=' ')
        sleep(0.5)
    print(f'Foram informados {len(núm)} valores ao todo.')
    print(f'O maior valor informado foi {m}.')
    sleep(2)


# Programa Principal
maior(2, 9, 4, 5, 7, 1)
maior(9, 4, 3, 3, 5)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
print('{:_^40}'.format('FIM'))
