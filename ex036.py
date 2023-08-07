print('\033[7;33m$\033[m'*32)
print('\033[7;33mAvaliador de Empréstimo Bancário\033[m')
print('\033[7;33m$\033[m'*32)
casa = float(input('\033[1;33mValor da casa:\033[m R$'))
salario = float(input('\033[1;33mSalário do comprador:\033[m R$'))
anos = int(input('\033[1;33mQuantos anos de financiamento?\033[m'))
n0 = casa / anos
n = n0 / 12
cde = 0.3 * salario
if cde < n:
    print('\033[1;33mPara pagar uma casa de\033[m \033[1;97mR${:.2f}\033[m\n\033[1;33mem\033[m \033[1;97m{}\033[m \033[1;33manos, '
          'a prestação será de\033[m \033[1;97mR${:.2f}\033[m'.format(casa, anos, n))
    print('Empréstimo \033[1;31mNEGADO\033[m!')
else:
    print('\033[1;33mPara pagar uma casa de\033[m \033[1;97mR${:.2f}\033[m \n\033[1;33mem\033[m \033[1;97m{}\033[m '
          '\033[1;33manos a prestação será de\033[m \033[1;97mR${:.2f}\033[m'.format(casa, anos, n))
    print('\033[1;33mO empréstimo pode ser\033[m \033[1;32mCONCEDIDO\033[m!')
print('\033[7;33m-\033[m'*20,'\033[1;33mVolte Sempre!\033[m','\033[7;33m-\033[m'*20)