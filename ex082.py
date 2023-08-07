lista = []
pares = list()
impares = list()
while True:
    n = int(input('Digite um número:'))
    lista.append(n)
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)
    continuar = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
    if continuar in 'N':
        print('.' * 50)
        print(f'Lista completa ↠ {lista}')
        print(f'    Pares      ↠ {pares} ')
        print(f'    Ímpares    ↠ {impares}')
        break
    elif continuar in 'S':
        print('-' * 50)
    else:
        continuar = str(input('Deseja continuar? [S/N] ', end='')).upper().strip()[0]
