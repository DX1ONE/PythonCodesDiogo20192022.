n1 = int(input('\033[1;31mPrimeiro número:'))
n2 = int(input('Segundo número:'))
n3 = int(input('Terceiro número:\033[m'))
# Verificando quem é o menor
menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3
# Verificando quem é o maior
maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3
print('O menor valor digitado foi \033[1;35m{}\033[m'.format(menor))
print('O maior valor digitado foi \033[1;35m{}\033[m'.format(maior))
