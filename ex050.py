soma = 0
for c in range(1, 7):
    valor = int(input(('Digite um número inteiro:')))
    if valor % 2 == 0:
        soma += valor
print('A soma dos PARES digitados é igual a: {}'.format(soma))