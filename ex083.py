lista = []
expressao = input('Digite a sua expressão: ').strip()
for elemento in expressao:
    lista.append(elemento)
if lista.count('(') == lista.count(')'):
    print('Sua expressão está válida!')
else:
    print('Sua expressão está errada!')
