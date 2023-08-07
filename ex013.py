si=float(input('\033[4;31mDigite o salário atual:\033[m'))
c1= si  * (15/100)
c2= si + c1
print('\033[1;31mO salário inicial era de:\033[m{} \033[1;31mreais. \nO salário com 15% de aumento é de :\033[m {}\033[1;31mreais.\033[m'.format(si,c2))