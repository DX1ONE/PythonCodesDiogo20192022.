lista = []
dados = []
pesomaior = []
pesomenor = []
nomemaior = []
nomemenor = []
cont = 0

while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso: ')))
    lista.append(dados[:])
    dados.clear()

    for pos, info in enumerate(lista):
        if pos == 0:
            pesomaior.append(info[1])
            pesomenor.append(info[1])
            nomemaior.append(info[0])
            nomemenor.append(info[0])

        else:
            for p in pesomaior:
                if info[1] > p:
                    pesomaior.clear()
                    nomemaior.clear()
                    pesomaior.append(info[1])
                    nomemaior.append(info[0])

                elif info[1] == p:
                    nomemaior.append(info[0])

                else:
                    if info[1] < p:
                        for elem in pesomenor:
                            if len(pesomenor) > 1 and elem == pesomenor[len(pesomenor) - 1]:
                                pesomenor.pop()
                                nomemenor.pop()

            for r in pesomenor:
                if info[1] < r:
                    pesomenor.clear()
                    nomemenor.clear()
                    pesomenor.append(info[1])
                    nomemenor.append(info[0])
                elif info[1] == r:
                    nomemenor.append(info[0])
                    if nomemenor[len(nomemenor) - 1] == info[1]:
                        nomemenor.pop()

                else:
                    if info[1] > r:
                        for elem in pesomenor:
                            if len(pesomenor) > 1 and elem == pesomenor[len(pesomenor) - 1]:
                                pesomenor.pop()
                                nomemenor.pop()
                        for nome in range(0, len(nomemenor) - 1):
                            if len(nomemenor) > 1:
                                if nomemenor[len(nomemenor) - 1] == nome:
                                    nomemenor.pop()
                                    print(nomemenor)

    continuar = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
    if continuar in 'N':
        break

    elif continuar in 'S':
        print('-' * 50)

    else:
        continuar = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]

print('-' * 50)
print(f'Foram cadastradas {len(lista)} pessoas.')
print('-' * 50)

if len(nomemaior) == 1:
    print(f'O maior peso foi {pesomaior[0]:.2f} kg. ', end='')
    print(f'Peso de: {nomemaior[0]}')

else:
    print(f'O maior peso foi {pesomaior[0]:.2f} kg.Peso de', end='')
    for cont, n in enumerate(nomemaior):
        print(f' {n}', end='')
        tamanho = len(nomemaior)
        print(',' if cont < len(nomemaior) else '.', end='')
print('')
print('-' * 50)

if len(nomemenor) == 1:
    print(f'O menor peso foi {pesomenor[0]:.2f} kg.', end='')
    print(f'Peso de {nomemenor[0]}')

else:
    print(f'O menor peso foi {pesomenor[0]:.2f} kg.Peso de ', end='')
    for cont, m in enumerate(nomemenor):
        print(f' {m}', end='')
        print(f',' if cont < len(nomemenor) else '.', end='')
print('\n{:-^50}'.format('FIM'))

print(nomemenor)
print(len(nomemenor))