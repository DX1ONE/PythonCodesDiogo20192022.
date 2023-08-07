print('\033[1;34m-\033[m\033[1;33m-\033[m'*20)
print('         \033[1;35mGôgo´s Supermercados\033[m')
print('\033[1;33m-\033[n\033[1;34m-\033[m'*20)
preco = float(input('\033[1;35mPreço das compras:\033[m \033[32mR$\033[m'))
print('''\033[1;35mEscolha a forma de pagamento:\033[m
\033[7;34;40m[ 1 ]\033[m \033[1;34mÀ vista (dinheiro/cheque)\033[m
\033[7;33;40m[ 2 ]\033[m \033[1;33mÀ vista no cartão        \033[m
\033[7;34;40m[ 3 ]\033[m \033[1;34mem até 2x no cartão      \033[m
\033[7;33;40m[ 4 ]\033[m \033[1;33m3x ou mais no cartão     \033[m''')
pagamento = int(input('\033[1;35mO formato de pagamento escolhido será:\033[m'))
if pagamento == 1:
    preco = preco - (preco * 0.1)
    print('\033[1;35mCom esta forma de pagamento,\no preço do produto é de:\033[m ', end='')
    print('\033[1;34m{:.2f} reais\033[m - \033[1;34m(10% de Desconto)\033[m'.format(preco))
elif pagamento == 2:
    preco = preco - (preco * 0.05)
    print('\033[1;35mCom esta forma de pagamento,\no preço do produto é de:\033[m ', end='')
    print('\033[1;33m{:.2f} reais\033[m - \033[1;33m(5% de Desconto)\033[m'.format(preco))
elif pagamento == 3:
    parcela = preco / 2
    print('\033[1;35mSua compra será parcelada em \033[m\033[1;33m2x\033[m'
          ' \033[1;35mde\033[m \033[1;33mR${:.2f}\033[m \033[1;35mSEM JUROS\033[m. '.format(parcela))
    print('\033[1;35mCom esta forma de pagamento,\no preço do produto é de:\033[m ', end='')
    print('\033[1;34m{:.2f} reais\033[m - \033[1;34m(Sem Desconto)\033[m'.format(preco))
elif pagamento == 4:
    preco = preco + (preco * 0.2)
    totparc = int(input('\033[1;35mQuantas parcelas?\033[m'))
    parcela = preco / totparc
    print('\033[1;35mSua compra será parcelada em\033[m \033[1;33m{}x\033[m\033[1;35m de\033[m \033[1;33mR${:.2f}\033[m\033[1;35m COM JUROS.\033[m'.format(totparc, parcela))
    print('\033[1;35mCom esta forma de pagamento,\no preço do produto é de:\033[m ', end='')
    print('\033[1;33m{:.2f} reais\033[m - \033[1;33m(20% de Juros)\033[m'.format(preco))
else:
    print('\033[1;31mVocê não selecionou uma opção!\033[m')
    print('\033[1;31mTente Novamente!\033[m')
print('\033[1;30;45m__FIM__\033[m')
