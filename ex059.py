from time import sleep
n1 = float(input('\033[1;36mPrimeiro Valor:\033[m'))
n2 = float(input('\033[1;36mSegundo Valor:\033[m'))
acabar = 0
while acabar != 5:
    print('\033[1;36m.....MENU.....\033[m')
    print('''\033[1;36mEscolha uma das opções:\033[m
\033[7;36m[ 1 ]\033[m \033[1;36msomar\033[m
\033[7;36m[ 2 ]\033[m \033[1;36mmultiplicar\033[m
\033[7;36m[ 3 ]\033[m \033[1;36mmaior\033[m
\033[7;36m[ 4 ]\033[m \033[1;36mnovos números\033[m
\033[7;36m[ 5 ]\033[m \033[1;36msair do programa\033[m''')
    escolha = int(input('\033[1;36m»Opção:\033[m'))
    if escolha == 1:
        soma = n1 + n2
        print('\033[1;36mA soma dos valores\033[m \033[1;97m{}\033[m \033[1;36me\033[m \033[1;97m{}\033[m \033[1;36mé igual a\033[m \033[1;97m{}\033[m'.format(n1, n2, soma))
    elif escolha == 2:
        multiplicar = n1 * n2
        print('\033[1;36mMultiplicando os valores\033[m \033[1;97m{}\033[m \033[1;36me\033[m \033[1;97m{}\033[m\033[1;36m, o produto é\033[m \033[1;97m{}\033[m\033[1;36m.\033[m'.format(n1, n2, multiplicar))
    elif escolha == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print('\033[1;36mEntre estes valores, o maior é o\033[m \033[1;97m{}\033[m\033[1;36m.\033[m'.format(maior))
    elif escolha == 4:
            print('\033[1;36mEscolha novos valores,então:\033[m')
            n1 = int(input('\033[1;36mPrimeiro Valor:\033[m'))
            n2 = int(input('\033[1;36mSegundo Valor:\033[m'))
    elif escolha == 5:
        print('\033[1;36mFinalizando...\033[m')
        acabar = 5
    else:
        print('\033[1;31mOpção Inválida! Tente Novamente.\033[m')
    print('\033[4;36m+\033[m' * 40)
    sleep(2)
print('\033[1;36m.....Fim do Prgrama! Volte Sempre!.....\033[m')
