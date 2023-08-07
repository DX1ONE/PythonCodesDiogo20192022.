lista = []
while True:
    n = int(input('Digite um número:'))
    lista.append(n)
    continuar = str(input(f'Você quer continuar? [S/N] ')).upper().strip()[0]
    if continuar in 'S':
        print('-' * 50)
    elif continuar in 'N':
        break
    else:
        continuar = str(input('Você quer continuar? [S/N] ')).upper().strip()[0]
print('-' * 50)
lista.sort(reverse=True)
print(f'\033[1;97mForam digitados\033[m \033[1;31m{len(lista)}\033[m \033[1;97mnúmeros.\033[m')
print(f'\033[1;97mOs valores digitados em ordem decrescente são:\033[m \033[1;31m{lista}\033[m')
if 5 in lista:
    print('\033[1;97mO valor\033[m \033[1;31m5\033[m \033[1;97mfoi digitado e está na lista!\033[m')
else:
    print('\033[1;97mO valor\033[m \033[1;31m5\033[m \033[1;97mnão foi digitado e não está na lista!\033[m')
