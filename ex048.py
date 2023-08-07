soma = 0 # acumulador
cont = 0 # contador
for c in range(1, 501, 2):
    if c % 3 == 0:
        soma += c
        cont += 1
print('\033[1;97mA soma de todos os\033[m \033[1;35m{}\033[m'
      ' \033[1;97mvalores solicitados é\033[m \033[1;35m{}\033[m'.format(cont, soma))
# A soma entre todos os números ímpares múltiplos de 3 no intervalo de 1 até 500.
