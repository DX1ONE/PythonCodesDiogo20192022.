maior = homem = mulhermenor = cont = 0
print('\033[1;33m{:=^40}\033[m'.format('REGISTRE PESSOAS'))
while True:
    idade = int(input('\033[1;97mSua idade:\033[m'))
    if idade > 18:
        maior += 1
    sexo = str(input('\033[1;97mSexo: [M/F]\033[m')).upper().strip()[0]
    if sexo in 'Mm':
        homem += 1
    elif sexo in 'Ff':
        if idade < 20:
            mulhermenor += 1
    else:
        while sexo not in 'MmFf':
            sexo = str(input('\033[1;97mSexo: [M/F]\033[m')).upper().strip()[0]
            if sexo in 'Mm':
                homem += 1
            elif sexo in 'Ff':
                if idade < 20:
                    mulhermenor += 1
    cont += 1
    print('\033[1;33m=\033[m' * 40)
    escolha = str(input('\033[1;30;43mVocê quer continuar?\033[m \033[1;33m[S/N]\033[m '))
    print('\033[1;33m=\033[m' * 40)
    while escolha not in 'SsNn':
        print('\033[1;33m=\033[m' * 40)
        escolha = str(input('\033[1;30;43mVocê quer continuar?\033[m \033[1;33m[S/N]\033[m '))
        print('\033[1;33m=\033[m' * 40)
    if escolha in 'Nn':
        print('\033[1;33mRegistro finalizado!\033[m')
        print(f'\033[1;97mDas\033[m \033[1;33m{cont}\033[m \033[1;97mpessoas registradas com sucesso:\033[m'
              f'\n\033[1;33m{maior}\033[m \033[1;97mtem mais de 18 anos;\033[m'
              f'\n\033[1;33m{homem}\033[m \033[1;97msão homens;\033[m'
              f'\n\033[1;33m{mulhermenor}\033[m \033[1;97msão mulheres menores de 20 anos.\033[m')
        break
print('\033[1;33m{:-^40}\033[m'.format('FIM'))
