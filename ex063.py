print('\033[m~\033[m' * 30)
print('{:^30}'.format('\033[1;34mSequência de Fibonacci\033[m'))
print('~' * 30)
n = int(input('\033[1;34mDigite um número:\033[m'))
t1 = 0
t2 = 1
print('\033[1;34m~\033[m' * 30 )
print('\033[1;34m{}\033[m \033[1m→\033[m \033[1;34m{}\033[m'.format(t1, t2), end='')
cont = 3
while cont <= n:
    t3 = t1 + t2
    print(' → \033[1;34m{}\033[m'.format(t3), end='')
    t1 = t2
    t2 = t3
    cont += 1
print(' → \033[1;34mFIM\033[m')
print('\033[1;34m~\033[m' * 30)
