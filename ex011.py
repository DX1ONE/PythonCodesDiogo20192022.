l1=float(input('\033[33mDigite a largura da parede:\033[m'))
h=float(input('\033[33mDigite a altura da parede:\033[m'))
a= l1 * h
t= a / 2
print('A sua parede tem \033[31m{:.1f}\033[m metros quadrados. \n>Você precisará de \033[31m{:.1f}\033[m litros de tinta para pintá-la!'.format(a,t))