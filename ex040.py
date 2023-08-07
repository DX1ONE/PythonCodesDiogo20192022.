print('\033[1;97mBoletim Final\033[m')
print('\033[1;97m=\033[m'*20)
n1 = float(input('\033[1;97mPrimeira nota:\033[m'))
n2 = float(input('\033[1;97mSegunda nota:\033[m'))
media = (n1 + n2) / 2
print('\033[1;97mTirando as notas\033[m {} \033[1;97me\033[m {}\033[1;97m, a média do aluno é\033[m {}'.format(n1, n2, media))
if media < 5.0:
    print('\033[1;31mO aluno está REPROVADO\033[m')
# elif media >= 5.0 and media < 7:
elif 7 > media >= 5:
    print('\033[1;33mO aluno está de RECUPERAÇÃO\033[m')
elif media >= 7.0:
    print('\033[1;32mO aluno está APROVADO\033[m')
