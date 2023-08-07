print('\033[1;31m-=\033[m'*20)
print('\033[7;31mAnalisador de triângulos\033[m')
print('\033[1;31m-=\033[m'*20)
r1 = float(input('\033[1;35mPrimeiro segmento:\033[m'))
r2 = float(input('\033[1;35mSegundo segmento:\033[m'))
r3 = float(input('\033[1;35mTerceiro segmento:\033[m'))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('\033[1;35mOs segmentos acima\033[m \033[1;31mPODEM FORMAR\033[m \033[1;35mum triângulo!\033[1;35m')
else:
    print('\033[1;35mOs segmentos acima\033[1;35m \033[1;31mNÃO PODEM FORMAR\033[m \033[1;35mum triângulo.\033[1;35m')