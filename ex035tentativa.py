print(('-='*20))
print('Analisador de triângulos')
print('-='*20)
r1 = float(input('Primeira reta:'))
r2 = float(input('Segunda reta: '))
r3 = float(input('Terceira reta:'))
maior = r1
# Verificando quem é maior
if r2 > r1 and r2 > r3:
    maior = r2
if r3 > r1 and r3 > r2:
    maior = r3
# verificando quem é menor:
menor = r1
if r2 < r1 and r2 < r3:
    menor = r2
if r3 < r1 and r3 < r2:
    menor = r3
# Verificando quem é mediano
mediano = r1
if r2 > r1 and r2 < r3:
    mediano = r2
if r2 < r1 and r2 > r3:
    mediano = r2
if r3 > r1 and r3 < r2:
    mediano = r3
if r3 < r1 and r3 > r2:
    mediano = r3
if maior - mediano >= menor:
    print('As retas {},{} e {} NÃO PODEM FORMAR um triângulo.'.format(r1, r2, r3))
if maior - mediano < menor:
    print('As retas {},{} e {} PODEM FORMAR um triângulo.'.format(r1, r2, r3))
