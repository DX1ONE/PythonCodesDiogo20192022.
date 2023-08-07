from datetime import date
ano = int(input('\033[1;97mAno de Nascimento do Atleta:\033[m'))
atual = date.today().year
idade = atual - ano
print('\033[1;97mO atleta tem {} anos.\033[m'.format(idade))
if idade <= 9:
    print('\033[1;97mA categoria deste atleta é:\033[m \033[1;35mMIRIM\033[m')
elif idade <= 14:
    print('\033[1;97mA categoria deste atleta é:\033[m \033[1;34mINFANTIL\033[m')
elif idade <= 19:
    print('\033[1;97mA categoria deste atleta é:\033[m \033[1;32mJUNIOR\033[m')
elif idade <= 25:
    print('\033[1;97mA categoria deste atleta é:\033[m \033[1;33mSÊNIOR\033[m')
else:
    print('\033[1;97mA categoria deste atleta é:\033[m \033[1;31mMASTER\033[m')