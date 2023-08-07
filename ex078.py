valores = []
for v in range(0, 5):
    valores.append(int(input(f'Digite um valor para a posição {v}:')))

    if v == 0:
        mai = men = valores[v]
    else:
        if valores[v] > mai:
            mai = valores[v]
        if valores[v] < men:
            men = valores[v]

print('=' * 50)
print(f'Você digitou os valores: {valores}')
print(f'O maior valor digitado foi {mai} nas posições ', end='')

for i, v in enumerate(valores):
    if v == mai:
        print(f'{i} ', end='')

print()
print(f'O menor valor digitado foi {men} nas posições ', end='')

for i, v in enumerate(valores):
    if v == men:
        print(f'{i} ', end='')
print()
