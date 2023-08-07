v = int(input('Qual é a \033[1;33mvelocidade\033[m do seu carro agora?:'))
vmp = 80
m = 7 * (v - vmp)
if v > vmp:
    print('\033[1;31mVocê ultrapassou o limite de velocidade da via!\033[m')
    print('\033[7;31mVocê foi multado!\033[m')
    print('Sua multa \033[4;97ma ser paga\033[m será de \033[1;31m{}\033[m reais.'.format(m))
else:
    print('\033[1;32mParabéns, você está dirigindo em uma velocidade correta!\033[m')
