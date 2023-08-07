n = list()
maior = 0
for c in range(1, 6):
    valor = int(input('Digite um valor:'))
    if c == 1 or valor > max(n):
        n.append(valor)
        print('Adicionado ao final da lista!')
        maior += 1
    elif c > 1:
        if valor < min(n):
            n.insert(0, valor)
            print('Adicionado na posição 0 da lista!')
        elif valor > min(n):
            if valor > n[+2]:
                n.insert(n.index(min(n)) , valor)
                print(f'Adicionado na posição {n.index(min(n)) + 1} da lista')
            else:
                n.insert(n.index(min(n)), valor)
                print(f'Adicionado na posição {n.index(min(n)) + 2}')
        elif valor < max(n):
            if valor < n[-2]:
                n.insert(n.index(max(n)), valor)
                print(f'Adicionado na posição {n.index(max(n)) - 2} da lista')
            else:
                n.insert(n.index(max(n)) , valor)
                print(f'Adicionado na posição {n.index(max(n)) - 1} da lista')

print(f'Os valores digitados foram: {n}')

# Obs.: Este código não está funcionando corretamente!



