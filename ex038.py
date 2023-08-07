n1 = int(input('\033[1;34mPrimeiro número:\033[m'))
n2 = int(input('\033[1;33mSegundo número:\033[m'))
maior = n1
if n2 > n1:
    maior = n2
    print('O \033[1;33mSegundo\033[m valor é maior.')
elif n1 > n2:
    print('O \033[1;34mPrimeiro\033[m valor é maior.')
else:
    print('\033[1;31mNão existe valor maior, os dois são iguais.\033[m')
