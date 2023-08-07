nome = str(input('\033[1;31mDigite seu nome:\033[m')).strip()
# nome = ((n.lower()).find('Silva'))
print('Seu nome tem Silva? \033[1;31m{}\033[m'.format('SILVA' in nome.upper()))
