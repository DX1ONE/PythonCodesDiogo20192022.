print('\033[1;97m-\033[m'*20)
print('\033[1;97m{:^20}\033[m'.format('Números primos'))
print('\033[1;97m-\033[m'*20)
n = int(input('\033[1;97mDigite um número:\033[m'))
p = 0  # contador
for c in range(1, n + 1):
    primo = n % c
    if primo == 0:
        print('\033[1;33m{}\033[m '.format(c), end='')
        p += 1
    elif primo != 0:
        print('\033[1;31m{}\033[m '.format(c), end='')
print('\n\033[1;97mO número\033[m \033[1;33m{}\033[m \033[1;97mfoi divisível\033[m'
      ' \033[1;33m{}\033[m \033[1;97mvezes.\033[m'.format(n, p))
if p != 2:
    print('\033[1;97mE por isso ele\033[m \033[1;31mNÃO É PRIMO\033[m\033[1;97m.\033[m')
elif p == 2:
    print('\033[1;97mE por isso ele é\033[m \033[1;32mPRIMO\033[m\033[1;97m.\033[m')
