tupla = (int(input('Digite um valor:')),
 int(input('Digite um valor:')),
 int(input('Digite um valor:')),
 int(input('Digite um valor:')))
print(f'Os valores digitados foram: {tupla}')
print(f'O valor 9 apareceu {tupla.count(9)} vez(es)')
posicao = 3
if posicao not in tupla:
    print('O valor 3 não foi digitado em nenhuma posição')
else:
    print(f'A primeira aparição do 3 foi na {tupla.index(3) + 1}ª posição.')
print('Os números pares digitados foram', end=' ')
for n in tupla:
    if n % 2 == 0:
        print(n, end=' ')
