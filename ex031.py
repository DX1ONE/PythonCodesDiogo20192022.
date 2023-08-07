d = int(input('\033[1;36mQual será a distância da sua viagem?\033[m'))
if d <= 200:
    curta = d * 0.50
    print('\033[1;33mO preço da sua viagem será de\033[m \033[7;33m{}\033[m \033[1;33mreais.\033[m'.format(curta))
else:
    longa = d * 0.45
    print('\033[1;33mO preço da sua viagem será de\033[m \033[7;33m{}\033[m \033[1;33mreais.\033[m'.format(longa))
print('\033[7;36m_____Boa Viagem!_____\033[m')