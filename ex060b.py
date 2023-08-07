from math import factorial
n = int(input('\033[1;97mDigite um número:\033[m'))
print('\033[1;33m{}! = \033[1;33m'.format(n), end='')
f = factorial(n)
for c in range(n, 0 , -1):
    print('\033[1;33m{}\033[m'.format(c), end='')
    print('\033[1;31m x \033[m'if c >1 else ' = ', end='')
print('\033[1;33m{}\033[m'.format(f), end='')
print('\n\033[1;97mx_FIM_x\033[m')