from datetime import date
atual = date.today().year
simbolo = '~'
print('\033[1;33m{}\033[m'
      '\033[1;32m{}\033[m'
      '\033[1;33m{}\033[m'
      '\033[1;32m{}\033[m'
      '\033[1;33m{}\033[m'
      '\033[1;32m{}\033[m'
      '\033[1;33m{}\033[m'
      '\033[1;32m{}\033[m'
      '\033[1;33m{}\033[m'
      '\033[1;32m{}\033[m'.format(simbolo,
                                  simbolo,
                                  simbolo,
                                  simbolo,
                                  simbolo,
                                  simbolo,
                                  simbolo,
                                  simbolo,
                                  simbolo,
                                  simbolo),
      '\033[1;33mAlistamento Militar - verificador de prazo\033[m '
      '\033[1;33m{}\033[m'
      '\033[1;32m{}\033[m'
      '\033[1;33m{}\033[m'
      '\033[1;32m{}\033[m'
      '\033[1;33m{}\033[m'
      '\033[1;32m{}\033[m'
      '\033[1;33m{}\033[m'
      '\033[1;32m{}\033[m'
      '\033[1;33m{}\033[m'
      '\033[1;32m{}\033[m'.format(simbolo,
                                  simbolo,
                                  simbolo,
                                  simbolo,
                                  simbolo,
                                  simbolo,
                                  simbolo,
                                  simbolo,
                                  simbolo,
                                  simbolo))
sexo = str(input('\033[1;33mQual é o seu sexo:\033[m')).upper()
if 'MASCULINO' in sexo:

    idade = int(input('\033[1;33mAno de nascimento:\033[m'))
    i = atual - idade
    print('\033[1;33mQuem nasceu em \033[1;32m{}\033[m \033[1;33mtem\033[m \033[1;32m{}\033[m \033[1;33manos em\033[m \033[1;32m{}\033[m\033[1;33m.\033[m'.format(idade, i, atual))
    # O ano atual é 2023
    if i < 18:
        saldo = 18 - i
        print('\033[1;33mVocê ainda irá se alistar no serviço militar!\033[m')
        print('\033[1;33mFalta\033[m \033[1;32m{}\033[m \033[1;33mano(s) para você se alistar.\033[m'.format(saldo))
        ano = atual + saldo
        print('\033[1;33mSeu alistamento será em\033[m \033[1;32m{}\033[m\033[1;33m.\033[m'.format(ano))

    elif i == 18:
        print('\033[1;32mEstá na hora de você se alistar!\033[m')
        print('\033[1;32mVocê deve se apresentar ao quartel mais próximo ainda este ano.\033[m')
    elif i > 18:
        saldo = i - 18
        print('\033[1;31mVocê ja devia ter se alistado!\033[m')
        print('\033[1;33mVocê excedeu\033[m \033[1;31m{}\033[m \033[1;33mano(s) do prazo de alistamento.\033[m'.format(saldo))
        ano = atual - saldo
        print('\033[1;33mSeu alistamento foi em\033[m \033[1;31m{}\033[m\033[1;33m.\033[m'.format(ano))
elif 'FEMININO' in sexo:
    print('\033[1;33mVocê não precisa se alistar!\033[m')
else:
    print('\033[1;31mVocê não colocou seu sexo.\nTente Novamente!\033[m')
print('\033[1;32m_\033[m'*20, '\033[1;33mFIM\033[m', '\033[1;32m_\033[m'*20)
