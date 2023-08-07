n1=float(input('\033[31mDigite uma metragem:\033[m'))
cm= n1 * 100
ml= n1 * 1000
print('O valor de \033[7;31m{}\033[m \033[4mmetros\033[m, é o mesmo que \033[7;31m{}\033[m \033[4mcentímetros\033[m e \033[7;31m{}\033[m \033[4mmilímetros\033[m!'.format(n1,cm,ml))