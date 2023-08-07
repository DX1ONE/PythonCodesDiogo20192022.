media = 0
velho = 0
anos = 0
men = ''
for c in range(1, 5):
    print('\033[1;34m----- {}ª Pessoa -----\033[m'.format(c))
    nome = str(input('\033[1;30;44mNome:\033[m')).strip()
    idade = int(input('\033[1;30;44mIdade:\033[m'))
    sexo = str(input('\033[1;30;44mSexo  [M/F]:\033[m')).upper().strip()
    if media == 0:
        media = idade
    elif media != 0:
        media += idade
    im = media / 4
    if sexo == 'M':
        if c == 1:
            velho = idade
            men = nome
        elif c != 1:
            if idade > velho:
                velho = idade
                men = nome
            elif idade < velho:
                velho = velho
    elif sexo == 'F':
        if idade >= 20:
            anos += 0
        elif idade < 20:
            anos += 1
print('\033[1;34mA média de idade é de\033[m \033[1;33m{:.1f}\033[m \033[1;34manos.\033[m'.format(im))
print('\033[1;34mO homem mais velho tem\033[m \033[1;33m{}\033[m \033[1;34manos e se chama\033[m \033[1;33m{}\033[m'.format(velho, men))
print('\033[1;34mEntre essas pessoas, há\033[m \033[1;33m{}\033[m \033[1;34mmulher(es)\033[m \033[1;33mmenor(es) de 20 anos.\033[m'.format(anos))
