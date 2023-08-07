lista = []
media = []
m = 0
mulher = []
dados = []
maior = []

while True:
    pessoa = {}
    n = str(input('Nome: '))
    pessoa['Nome'] = n
    s = str(input('Sexo: ')).strip().upper()[0]

    if s in 'MF':
        pessoa['Sexo'] = s

    else:
        while True:
            print('ERRO! Por favor, digite apenas M ou F.')
            s = str(input('Sexo: ')).strip().upper()[0]
            if s in 'MF':
                pessoa['Sexo'] = s
                break

    i = int(input('Idade: '))
    pessoa['Idade'] = i
    lista.append(pessoa.copy())
    del pessoa

    continuar = str(input('Deseja continuar? [S/N]')).strip().upper()[0]
    if continuar in 'N':
        break
    elif continuar not in 'SN':
        while continuar not in 'SN':
                print('ERRO! Por favor, digite apenas S ou N.')
                continuar = str(input('Deseja continuar? [S/N]')).strip().upper()[0]

print('—' * 50)
print(f'Foram cadastradas {len(lista)} pessoas.')
for cont, n in enumerate(lista):
    media.append(lista[cont]['Idade'])
    for contagem, v in enumerate(media):
        if contagem == 0:
            m = v
        else:
            m += v

mediana = m / len(media)
print('–' * 50)
print(f'A media das idades é de {mediana} anos.')
for cont, n in enumerate(lista):
    if lista[cont]['Sexo'] == 'F':
        dados.append(lista[cont]['Nome'])
        dados.append(lista[cont]['Idade'])
        mulher.append(dados[:])
        dados.clear()

print('—' * 50)
print(f'As mulheres cadastradas foram ', end='')
for m in mulher:
    print(f'{m}', end='')
    print(', ' if cont < len(maior) - 1 else '.')
for cont, v in enumerate(lista):
    if lista[cont]['Idade'] > mediana:
        maior.append(lista[cont])

print('\n', '–' * 50)
print(f'As pessoas com idade superior à media são: \n', end='')
for cont, n in enumerate(maior):
    print(f'Nome = {maior[cont]["Nome"]}; Sexo = {maior[cont]["Sexo"]}; Idade = {maior[cont]["Idade"]}', end='')
    print(', ' if cont < len(maior) - 1 else '.')
print('{:×^50}'.format('FINALIZADO'))
