print('\033[1;35m-\033[m' * 50)
print('\033[1;97;45m{:^50}\033[m'.format('Supermercado Python'))
print('\033[1;35m-\033[m' * 50)
total = mais = barato = preçobarato = 0
while True:
    nome = str(input('\033[1;35mNome do Produto:\033[m'))
    while nome == '':
        print('\033[1;31mSlot Vazio! Tente Novamente.\033[m')
        nome = str(input('\033[1;35mNome do Produto:\033[m'))
    if barato == 0:
        barato = nome
    preço = float(input('\033[1;35mPreço do Produto:\033[m'))
    if preçobarato == 0:
        preçobarato = preço
    elif preçobarato != 0:
        if preço < preçobarato:
            preçobarato = preço
    while preço == '':
        print('\033[1;31mSlot Vazio! Tente Novamente.\033[m')
        preço = float(input('\033[1;35mPreço do Produto:\033[m'))
    if preço > 1000:
        mais += 1
    elif preço == preçobarato:
        barato = nome
    print('\033[1;35m{:-^50}\033[m'.format('Produto Registrado!'))
    total += preço
    continuar = str(input('\033[1;35mQuer continuar? [S/N]\033[m')).upper().strip()[0]
    print('\033[1;35m-\033[m' * 50)
    while continuar == '':
        print('\033[1;31mSlot Vazio! Preencha o campo.\033[m')
        continuar = str(input('\033[1;35mQuer continuar? [S/N]\033[m', end='')).upper().strip()[0]
    if continuar in 'Ss':
        print('', end='')
    elif continuar in 'Nn':
        print('\033[1;97;45m{:-^50}\033[m'.format('FIM DO REGISTRO'))
        print(f'\033[1;35mPreço final da(s) compra(s):\033[m \033[1;97mR${total:.2f}\033[m')
        print(f'\033[1;35mCusta(m) mais de R$1000.00:\033[m \033[1;97m{mais} produto(s)\033[m')
        print(f'\033[1;35mMais barato:\033[m \033[1;97m{barato}\033[m \033[1;35mque custa\033[m \033[1;97mR${preçobarato:.2f}\033[m')
        print('\033[1;35m{:-^50}\033[m'.format(''))
        break
    else:
        print('\033[1;31mOpção Inválida! Tente Novamente.\033[m')
