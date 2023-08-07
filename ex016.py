import math
from  math import trunc
n1=float(input('\033[1;30;107mDigite um número com partes decimais:\033[m'))
print('\033[1;97mO número\033[m \033[1;30;107m{}\033[m\033[1;97m,tem como porção inteira:\033[m \033[1;30;107m{}\033[m '.format(n1,math.trunc(n1)))