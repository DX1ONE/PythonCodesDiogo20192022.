a = float(input('Primeiro segmento:'))
b = float(input('Segundo segmento:'))
c = float(input('Terceiro segmento:'))
if a < b + c and b < a + c and c < a + b:
    print('Esses segmentos PODEM formar um triângulo ', end='')
    if a == b == c:
        print('EQUILÁTERO')
    elif a != b != c != a:
        print('ESCALENO!')
    else:
        print('ISÓSCELES!')

else:
    print('Estes segmentos NÃO PODEM formar um triângulo.')
