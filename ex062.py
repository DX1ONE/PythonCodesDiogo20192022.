t = int(input('\033[1;31mPrimeiro Termo:\033[m'))
r = int(input('\033[1;31mRazão da PA:\033[m'))
termo = t
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print('\033[1;31m{}\033[m \033[1;97m→ \033[m'.format(termo), end='')
        termo += r
        cont += 1
    print('\033[1;97mPAUSA\033[m')
    mais = int(input('\033[1;31mQuantos termos você quer mostrar a mais?\033[1;31m'))
print('\033[1;97m-\033[m' * 50)
print('\033[1;31mProgressão finalizada com\033[m \033[1;97m{}\033[m \033[1;31mtermos mostrados.\033[m'.format(total))
print('\033[1;97m-\033[m' * 50)