maior = 0
menor = 0
for p in range(1, 6):
    peso = float(input('\033[1;35mPeso da\033[m \033[1;97m{}ª\033[m \033[1;35mpessoa:\033[m'.format(p)))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('\033[1;35mO maior peso é o\033[m \033[1;97m{}\033[m'.format(maior))
print('\033[1;35mO menor peso é o\033[m \033[1;97m{}\033[m'.format(menor))
