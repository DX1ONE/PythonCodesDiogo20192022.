lista = [[], []]
for n in range(1, 8):
    num = int(input('Digite um número: '))
    if num % 2 == 0:
        lista[0].append(num)

    else:
        lista[1].append(num)

lista[0].sort()
lista[1].sort()
print(f'Os pares digitados foram {lista[0]} e os ímpares{lista[1]}')
