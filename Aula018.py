teste = list()
teste.append('Diogo')
teste.append(18)
galera = list()
galera.append(teste[:])
teste[0] = 'Gustavo'
teste[1] = 40
galera.append(teste[:])
print(galera)