n = cont = soma = 0
n = int(input('\033[1;30;46mDigite um número [999 p/ parar]:\033[m'))
while n != 999:
    soma += n
    cont += 1
    n = int(input('\033[1;30;46mDigite um número [999 p/ parar]:\033[m'))
print('\033[1;36mForam digitados\033[m \033[1;97m{}\033[m \033[1;36mnúmeros.\033[m'.format(cont))
print('\033[1;36mA soma entre os números digitados é igual a\033[m \033[1;97m{}\033[m'.format(soma))
print('\033[1;36m{:_^48}\033[m'.format('FIM'))
