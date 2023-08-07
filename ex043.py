print('\033[1;31mI\033[m\033[1;33m-\033[m\033[1;31mM\033[m\033[1;33m-\033[m\033[1;31mC\033[m\033[m\033[1;33m-\033[m'*10)
print('                 \033[7;33mÍNDICE DE MASSA CORPORAL\033[m')
print('\033[1;31mI\033[m\033[1;33m-\033[m\033[1;31mM\033[m\033[1;33m-\033[m\033[1;31mC\033[m\033[1;33m-\033[m'*10)

peso = float(input('\033[1;31mQual é o seu peso? Kg\033[m'))
altura = float(input('\033[1;31mQual é a sua altura? m\033[m'))
imc = peso / (altura.__pow__(2))
if imc < 18.5:
    print('O seu \033[1;31mIMC\033[m é \033[1;31m{:.1f}\033[m,e você está \033[1;33mABAIXO DO PESO\033[m'.format(imc))
elif 18.5 <= imc < 25:
    print('O seu \033[1;31mIMC\033[m é \033[1;31m{:.1f}\033[m,e você está no \033[1;92mPESO IDEAL\033[m'.format(imc))
elif 25 <= imc < 30:
    print('O seu \033[1;31mIMC\033[m é \033[1;31m{:.1f}\033[m,e você está com \033[1;33mSOBREPESO\033[m'.format(imc))
elif 30 <= imc <= 40:
    print('O seu \033[1;31mIMC\033[m é \033[1;31m{:.1f}\033[m,e você está com \033[1;31mOBESIDADE\033[m'.format(imc))
elif imc > 40:
    print('O seu \033[1;31mIMC\033[m é \033[1;31m{:.1f}\033[m,e você está com '
          '\033[1;30;41mOBESIDADE MÓRBIDA\033[m'.format(imc))
print('\033[7;33mFIM\033[m')
