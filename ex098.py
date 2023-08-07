from time import sleep


def contador(i, f, p):
    print('-=' * 20)
    if p < 0:
        p *= -1
    elif p == 0:
        p += 1
    else:
        p = p
    print(f'Contagem de {i} até {f} de {p} em {p}')
    sleep(2.5)
    if i < f:
        cont = i
        lista = []
        while cont <= f:
            lista.append(cont)
            if p == 0:
                cont += 1
            elif p < 0:
                cont -= p
            else:
                cont += p
        for n in lista:
            print(f'{n}', end=' ')
            sleep(0.5)
        print('FIM!')

    else:
        contagem = i
        while contagem >= f:
            print(f'{contagem} ', end='')
            contagem -= p
            sleep(0.5)
        print('FIM!')


# Programa Principal
contador(1, 10, 1)
contador(10, 0, 2)
print('-=' * 20)
print('Agora é sua vez de personalizar a contagem!')
inicio = int(input('Início: '))
fim = int(input('Fim   : '))
passo = int(input('Passo : '))
contador(i=inicio, f=fim, p=passo)
print(' <<<<<<<<<<<<<VOLTE SEMPRE!>>>>>>>>>>>>>')

# Antes do gabarito, não estava funcionando o caso (i = 12, f = -10, p = 7)
