print('-' * 50)
print('{:^50}'.format('LISTAGEM DE PREÇOS'))
print('-' * 50)
listagem = ('Lápis', 1.75,
            'Borracha', 2.00,
            'Caderno', 15.90,
            'Estojo', 25.00
            , 'Trasferidor',4.20,
            'Compasso', 9.99,
            'Mochila', 120.32,
            'Canetas', 22.30
            , 'Livros', 34.90)
for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<40}', end='')
    else:
        print(f'R$ {listagem[pos]:>5.2f}')
print('-' * 50)
