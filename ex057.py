sexo = str(input('\033[1;97mInforme seu sexo: [M/F]\033[m ')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo =str(input('\033[1;31mDados Inválidos .Por favor, informe seu sexo:\033[m')).strip().upper()[0]
print('\033[1;97mSexo\033[m \033[1;32m{}\033[m \033[1;97mregistrado com sucesso.\033[m'.format(sexo))
print('\033[1;97mObrigado!\033[m')
