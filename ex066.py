s = c = 0
while True:
    n = int(input('\033[1;97mDigite um número [999 p/ parar]:\033[m '))
    if n == 999:
        break
    s += n
    c += 1
print(f'\033[1;33mForam digitados \033[1;97m{c}\033[m \033[1;33mnúmeros e a soma entre eles é igual a\033[m \033[1;97m{s}\033[m\033[1;33m.\033[m')
