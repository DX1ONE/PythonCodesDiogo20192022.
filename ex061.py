from time import sleep
soma = 0
print('\033[1;97m.\033[m' * 54)
t = int(input('\033[1;97mDigite um valor:\033[m'))
print('\033[1;97m.\033[m' * 54)
r = int(input('\033[1;97mRazão da PA:\033[m'))
print('\033[1;97m.\033[m' * 54)
pa = t + r
sleep(1)
print('\033[1;97mA \033[1;31mPA\033[m \033[1;97mdo número\033[m \033[1;31m{}'
      '\033[m \033[1;97maté o 10º termo usando a razão\033[m \033[1;31m{}\033[m \033[1;97mé:\033[m'
      '\n '.format(t, r), end='')
while soma < 10:
    print('\033[1;31m{}\033[m'.format(pa), end='')
    print('\033[1;97m , \033[m'if soma < 9 else '\033[1;97m . \033[m', end='')
    soma += 1
    pa += r
print('\n\033[1;97m{:.^54}\033[m'.format('FIM'))
