from time import sleep
print('—' * 50)
print('{:^50}'.format('ATM'))
print('—' * 50)
saque = int(input('Qual valor você quer sacar? R$'))
print('Processando...')
sleep(2)
print('—' * 50)
cinquenta = saque // 50
multiplo = saque - (cinquenta * 50)
vinte = multiplo // 20
mult = multiplo - (20 * vinte)
dez = mult // 10
m = mult - (10 * dez)
um = m // 1
multip = m - (1 * um)
if cinquenta > 0:
    print(f'Cédulas de R$50: {cinquenta}')
    if vinte > 0 :
        print(f'Cédulas de R$20: {vinte}')
    elif dez > 0:
        print(f'Cédulas de R$10: {dez}')
        if dez > 0:
            print(f'Cédulas de R$10: {dez}')
        elif um > 0:
            print(f'Cédulas de R$1 : {um}')
elif vinte > 0 :
        print(f'Cédulas de R$20: {vinte}')
elif dez > 0:
        print(f'Cédulas de R$10: {dez}')
elif um > 0:
        print(f'Cédulas de R$1 : {um}')
print('—' * 50)