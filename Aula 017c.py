a = [2, 3, 4, 7]
b = a[:] # cópia de listas
# b = a  ligação de listas
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')