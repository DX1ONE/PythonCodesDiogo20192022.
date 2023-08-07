print('\033[1;33m{:^8}\033[m'.format('ARARA')*5)
print('\033[1;30;43m{:^40}\033[m'.format('Identificador de Palíndromos'))
print('\033[1;33m{:^5}\033[m'.format('OVO')*8)
print('\033[1;35m-> Não acentue a frase!\033[m')
frase = str(input('\033[1;35mDigite um frase:\033[m')).strip().upper()
j = frase.split()
jm = ''.join(j)
jc = jm[::-1]
print('\033[1;35mO inverso de\033[m \033[1;97m{}\033[n \033[1;35mé\033[m \033[1;97m{}\033[m'.format(jm, jc))
print('\033[1;35m{}\033[m'.format('-')*40)
if jm == jc:
    print('\033[1;32mEsta frase é um PALÍNDROMO!\033[m')
else:
    print('\033[1;31mA frase digitada NÃO é um palíndromo.\033[m')
print('\033[1;35m{}\033[m'.format('-') * 40)
# Exemplos de palíndromo:
# apos a sopa
# a sacada da casa
# a torre da derrota
# o lobo ama o lobo
# anotaram a data da maratona
