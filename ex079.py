números = []

while True:
    n = int(input('Digite um valor:'))

    if n not in números:
        números.append(n)
        print('Valor adicionado com sucesso!')
    else:
        print('Valor duplicado! Não vou adicionar...')
    r = str(input('Você quer continuar? [S/N] '))
    if r in 'Nn':
        break
print('-' * 50)
números.sort()
print(f'Você digitou os valores: {números}')
