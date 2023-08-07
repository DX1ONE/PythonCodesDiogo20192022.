import random
print('Estou pensando em um número de \033[1;35m0 a 5\033[m \n\033[4;35mTente adivinhar!\033[m')
a = random.randint(0, 5)
e = int(input('\033[1;97mEscolha um número de 0 a 5:\033[m'))
if e == a:
    print('\033[1;32mParabéns,você acertou!\033[m')
else:
    print('\033[1;31mNão foi dessa vez...\033[m')
print('\033[36m___FIM___\033[m')
