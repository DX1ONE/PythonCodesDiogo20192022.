from random import randint
from time import sleep
sorte = []
dados = []
tot = 1
print('\033[1;97m—\033[m' * 50)
print('\033[1;32m{:^50}\033[m'.format('MEGA SENA'))
print('\033[1;97m—\033[m' * 50)

jogos = int(input('\033[1;32mQuantos jogos você deseja? \033[m'))
print('\033[1;97m—\033[m' * 50)

while tot <= jogos:
    contador = 0
    while True:
        num = (randint(1, 60))
        if num not in dados:
            dados.append(num)
            contador += 1
        if contador >= 6:
            break
    dados.sort()
    sorte.append(dados[:])
    dados.clear()
    tot += 1

for r in range(0, len(sorte)):
    print(f'\033[1;97mO \033[m \033[1;32m{r + 1}° \033[m \033[1;97mjogo  é \033[m \033[1;32m{sorte[r]}\033[m')
    print('\033[1;97m-\033[m' * 50 if r < len(sorte) - 1 else '\033[1;97m—\033[m' * 50)
    sleep(1)

print('\033[1;32m{:^50}\033[m'.format('BOA SORTE!'), end='')
