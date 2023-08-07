n = str(input('\033[36;107mDigite o nome de uma cidade:\033[m')).strip()
# s1 = n.split()
# santo = s1[0]
# print('Santo'in santo)

print('O nome da cidade começa com Santo? \033[1;32m{}\033[m'.format(n[:5] == 'Santo'))
