from random import shuffle
n1 = str(input('\033[1;31mPrimeiro aluno:\033[m'))
n2 = str(input('\033[1;33mSegundo aluno:\033[m'))
n3 = str(input('\033[1;31mTerceiro aluno:\033[m'))
n4 = str(input('\033[1;33mQuarto aluno:\033[m'))
lista = [n1, n2, n3, n4]
shuffle(lista)
print('A ordem de apresentação será')
print('\033[1;34m',lista,'\033[m')