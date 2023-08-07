a = int(input('\033[4;36mEscreva um ano:\033[m'))
if a % 4 == 0:
    print('O ano \033[1;32m{}\033[m é bissexto.'.format(a))
else:
    print('O ano \033[1;31m{}\033[m não é bissexto.'.format(a))
