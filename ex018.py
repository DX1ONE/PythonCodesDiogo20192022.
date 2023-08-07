import math
a=int(input('\033[1;31mDigite um ângulo:\033[m'))
sen = math.sin(math.radians(a))
cos =(math.cos(math.radians(a)))
tan =(math.tan (math.radians(a)))
print('O seno, cosseno e a tangente do ângulo {} graus são  respectivamente: \n\033[1:31mSENO: {:.2f} \nCOSSENO: {:.2f} \nTANGENTE: {:.2f}\033[m '.format(a,sen,cos,tan))