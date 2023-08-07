print('\033[1;33m=\033[m' * 50)
print('\033[1;30;43m{:^50}\033[m'.format('Tabuada'))
print('\033[1;33m=\033[m' * 50)
tabuada = 0
while True:
    n = int(input('\033[1;33mDigite um valor para sua tabuada:\033[m'))
    if n < 0:
        break
    elif n >= 0:
        cont = 0
        while cont <= 10:
            tabuada = n * cont
            print(f'\033[1;97m{n}\033[m \033[1;33mvezes\033[m \033[1;97m{cont}\033[m \033[1;33m=\033[m ', end='')
            print(f'\033[1;97m{tabuada}\033[m')
            cont += 1
        print('\033[1;33m=\033[m' * 50)
print('\033[1;30;43m{:=^50}\033[m'.format('Programa Finalizado!'))