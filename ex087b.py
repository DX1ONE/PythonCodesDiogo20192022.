matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
sompar = mai = somcol = 0

for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))

print('—' * 50)

for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
        if matriz[l][c] % 2 == 0:
            sompar += matriz[l][c]
    print()
print('—' * 50)
print(f'A soma dos valores pares é {sompar}')
for l in range(0, 3):
    somcol += matriz[l][2]
print(f'A soma dos valores da terceira coluna é {somcol}')
for c in range(0, 3):
    if c == 0 or matriz[1][c] > mai:
        mai = matriz[1][c]

print(f'O maior valor da segunda linha é {mai}')
