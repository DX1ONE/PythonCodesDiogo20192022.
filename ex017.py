import math
from math import hypot
co=float(input('Coloque o valor do \033[0;97;45mcateto oposto:\033[m'))
ca=float(input('Coloque o valor do \033[0;97;45mcateto adjascente:\033[m'))
#h=((co ** 2)+(ca ** 2))** (1/2)
h=math.hypot(co,ca)
print('\033[0;35mO comprimento da hipotenusa do triângulo de catetos\033[m {}(oposto) \033[0;35me\033[m {}(adjascente) \033[0;35mvale:\033[m {:.2f}'.format(co,ca,h))