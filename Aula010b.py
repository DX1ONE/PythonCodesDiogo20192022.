n1 = float(input('Digite a primeira nota:'))
n2 = float(input('Digite a segunda nota:'))
m = (n1 + n2) / 2
f = ('FIM.')
print('A média foi de: {}'.format(m))
if m >= 6.0:
    print('Sua média foi BOA, PARABÉNS!')
else:
    print('Sua média foi RUIM, ESTUDE MAIS!')
print('{:^10}'.format(f))