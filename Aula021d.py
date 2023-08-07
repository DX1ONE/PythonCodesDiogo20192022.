def funcao(n2):
    global n1
    n1 = 8
    n2 += 4
    n3 = 2
    print(f'N1 dentro vale {n1}')
    print(f'N2 dentro vale {n2}')
    print(f'N3 dentro vale {n3}')


n1 = 5
funcao(n1)
print(f'N1 fora vale {n1}')
