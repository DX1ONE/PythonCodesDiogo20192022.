n = int(input('Digite um número inteiro:'))
print('''Escolha uma das bases de conversão:
\033[1;31m[ 1 ]\033[m converter para \033[1;31mBINÁRIO\033[m
\033[1;33m[ 2 ]\033[m converter para \033[1;33mOCTAL\033[m
\033[1;32m[ 3 ]\033[m converter para \033[1;32mHEXADECIMAL\033[m''')
opcao = int(input('Sua opção:'))
if opcao == 1:
    print('\033[1m{}\033[m convertido para \033[1;31mBINÁRIO\033[m é igual a \033[1;31m{}\033[m'.format(n, bin(n)[2:]))
elif opcao == 2:
    print('\033[1m{}\033[m convertido pra \033[1;33mOCTAL\033[m é igual a \033[1;33m{}\033[m'.format(n, oct(n)[2:]))
elif opcao == 3:
    print('\033[1m{}\033[m convertido para \033[1;32mHEXADECIMAL'
          '\033[m é igual a \033[1;32m{}\033[m'.format(n, hex(n)[2:]))
else:
    print('X'*5, '\033[4mOpção inválida.Tente novamente.\033[m', 'X'*5)
    