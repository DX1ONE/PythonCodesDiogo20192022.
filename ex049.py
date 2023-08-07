n1 = int(input('\033[1;33mDigite um número:\033[m'))
print('\033[1;33m{:=^20}\033[m'.format('Tabuada'))
for c in range(1, 11):
    print(' {} \033[1;33mvezes\033[m {} = \033[7;33m{}\033[m'.format(n1, c, n1 * c))
