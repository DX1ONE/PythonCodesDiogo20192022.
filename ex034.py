salario = int(input('\033[1;33mQual o valor do seu salário?\033[m'))
if salario > 1250:
    aumento = salario + (salario * 0.1)
    print('O seu novo salário será de \033[7;33m{:.1f} reais\033[m!'.format(aumento))
else:
    aumento = salario + (salario * 0.15)
    print('O seu novo salário será de \033[7;33m{:.1f} reais\033[m!'.format(aumento))
print('\033[7;30;43m$-FIM-$\033[m')
