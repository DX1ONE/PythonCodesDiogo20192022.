n1 = int(input('\033[1;97mDigite um número:\033[m'))
p = n1 % 2
if p == 0 :
    print('Este número é \033[7;97;40mpar\033[m')
else:
    print('Este número é \033[7;30;107mímpar\033[m')
