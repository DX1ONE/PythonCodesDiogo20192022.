def area(l, c):
    calc = l * c
    print(f'A área de um terreno {l} x {c} é de {calc:4.1f} m².')


def titulo(txt):
    print(txt)
    print('—' * 50)


# Programa Principal
titulo('Controle de Terrenos')
largura = float(input('LARGURA(m): '))
comprimento = float(input('COMPRIMENTO(m): '))
area(l=largura, c=comprimento)
titulo('                FIM')