nome = str(input('\033[1;97m Qual é o seu nome?\033[m'))
if nome == 'Diogo':
    print('\033[1;35mQue nome lindo!\033[m')
elif nome == 'Manu' or nome == 'Felipe' or nome == 'Luísa':
    print('\033[1;31mPelo seu nome você deve ser uma pessoa muito legal!\033[m')
elif nome in 'Maria Amanda Júlia Nicole Isadora':
    print('\033[1mBelo nome feminino!\033[m')
else:
    print('\033[1;37mSeu nome é bem normal.\033[m')
print('Tenha um bom dia, \033[1;34m{}\033[m!'.format(nome))