from random import choice
a1 = str(input('Qual o nome do \033[1;34mprimeiro\033[m aluno?'))
a2 = str(input('Qual o nome do \033[1;35msegundo\033[m aluno?'))
a3 = str(input('Qual o nome do \033[1;34mterceiro\033[m aluno ?'))
a4 = str(input('Qual o nome do \033[1;35mquarto\033[m aluno?'))
lista = [a1,a2,a3,a4]
sort = (choice(lista))
print('O aluno sorteado foi: \033[1;36m{}\033[m'.format(sort))