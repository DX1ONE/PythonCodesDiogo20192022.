lista = []
dados = []
mai = men = 0
while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso: ')))
    if len(lista) == 0:
        mai = men = dados[1]
    else:
        if dados[1] > mai:
            mai = dados[1]
        if dados[1] < men:
            men = dados[1]
    lista.append(dados[:])
    dados.clear()
    continuar = str(input('Deseja continuar? [S/N]')).strip().upper()[0]
    if continuar in 'N':
        break

print(f'Foram cadastradas {len(lista)} pessoas.')
print(f'O maior peso registrado foi {mai} Kg.Peso de ', end='')
for cont, p in enumerate(lista):
    if p[1] == mai:
        print(f'|{p[0]}| ', end='')

print(f'\nO menor peso registrado foi {men} Kg.Peso de ',end='')
for cont, p in enumerate(lista):
    if p[1] == men:
        print(f'|{p[0]}| ', end='')
print()
