palavras = ('aforismo', 'apeiron', 'leitura', 'ascetismo',
            'ataraxia', 'autonomia', 'caos', 'cartesianismo',
            'catarse', 'ceticismo', 'cinismo', 'empirismo')
for p in palavras:
    print(f'\nNa palavra {p.upper()} temos ', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')
