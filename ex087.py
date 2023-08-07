lista = []
pares = []
cont =  cnt = 0
n1 = int(input(f'Digite um valor para [0 , 0]: '))
lista.append(n1)
n2 = int(input(f'Digite um valor para [0 , 1]: '))
lista.append(n2)
n3 = int(input(f'Digite um valor para [0 , 2]: '))
lista.append(n3)
n4 = int(input(f'Digite um valor para [1 , 0]: '))
lista.append(n4)
n5 = int(input(f'Digite um valor para [1 , 1]: '))
lista.append(n5)
n6 = int(input(f'Digite um valor para [1 , 2]: '))
lista.append(n6)
n7 = int(input(f'Digite um valor para [2 , 0]: '))
lista.append(n7)
n8 = int(input(f'Digite um valor para [2 , 1]: '))
lista.append(n8)
n9 = int(input(f'Digite um valor para [2 , 2]: '))
lista.append(n9)

print(f'''[ {lista[0]} ] [ {lista[1]} ] [ {lista[2]} ]
[ {lista[3]} ] [ {lista[4]} ] [ {lista[5]} ]
[ {lista[6]} ] [ {lista[7]} ] [ {lista[8]} ]''')
for n in lista:
    if n % 2 == 0:
        pares.append(n)
for p in pares:
    cont += p
print(f'A soma dos valores pares é {cont}')
soma = lista[2] + lista[5] + lista[8]
print(f'A soma dos valores da terceira coluna é {soma}')
maior = 0
if lista[3] > maior:
    maior = lista[3]
if lista[4] > maior:
    maior = lista[4]
if lista[5] > maior:
    maior = lista[5]
print(f'O maior valor da segunda linha é {maior}')