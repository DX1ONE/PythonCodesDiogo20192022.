from random import randint
from time import sleep
n = randint(0, 10)
print('\033[1;97;40mSou seu computador...\033[m\n\033[1;97;40mAcabei de pensar em um número entre 0 e 10.\033[m')
print('\033[1;97;40mSerá que você consegue adivinhar qual foi?\033[m')
sleep(1)
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('\033[1;97;40mQual é o seu palpite?\033[m'))
    palpites += 1
    if jogador == n:
        acertou = True
    else:
        if jogador < n:
            print('\033[1;97;40mMais...Tente Novamente.\033[m')
            sleep(0.5)
        elif jogador > n:
            print('\033[1;97;40mMenos...Tente Novamente.\033[m')
            sleep(0.5)
print('\033[1;32mAcertou com\033[m \033[1;97m{}\033[m \033[1;32mtentativas. Parabéns!\033[m'.format(palpites))
