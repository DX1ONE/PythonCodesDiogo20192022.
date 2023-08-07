from time import sleep
notas = []
pessoa = []
lista = []
print('\033[1;32m•\033[m' * 50)
print('\033[1;97;42m{:^50}\033[m'.format('BOLETIM ESCOLAR'))
print('\033[1;32m•\033[m' * 50)
while True:
    pessoa.append(str(input('\033[1;32mNome do Aluno: \033[1;32m')))
    notas.append(float(input('\033[1;32mNota 1: \033[m')))
    notas.append(float(input('\033[1;32mNota 2: \033[m')))
    notas.append((notas[0] + notas[1]) / 2)
    pessoa.append(notas[:])
    lista.append(pessoa[:])
    notas.clear()
    pessoa.clear()
    continuar = str(input('\033[1;32mDeseja continuar?\033[m \033[1;97m[S/N]\033[m ')).strip().upper()[0]
    if continuar in 'N':
        print('\033[1;32m•\033[m' * 50)
        print('''\033[1;97mNo. Nome           MÉDIA\033[m
\033[1;32m------------------------\033[m''')
        for pos in range(0, len(lista)):
            print(f'\033[1;97m{pos}   {lista[pos][0]:<10}     {lista[pos][1][2]:.1f}\033[m')
        print('\033[1;32m-\033[m' * 24)
        print('\033[1;32m•\033[m' * 50)
        sleep(1)
        break
    elif continuar not in 'SN':
        continuar = str(input('\033[1;32mDeseja continuar?\033[m \033[1;97m[S/N]\033[m ')).strip().upper()[0]

while True:
    mais = int(input('\033[1;32mMostrar notas de qual aluno?\033[m \n\033[1;97m(Número negativo finaliza):\033[m '))
    sleep(1)
    if mais < 0:
        break
    elif mais >= 0:
        for cont, n in enumerate(lista):
            if mais == cont:
                print('\033[1;32m•\033[m' * 50)
                sleep(0.5)
                print(f'\033[1;97;42m          Notas de {lista[cont][0]} são {lista[cont][1][:2]}         \033[m')
                print('\033[1;32m•\033[m' * 50)
    elif mais > len(lista):
        print('\033[1;32mEste aluno não foi cadastrado!\033[m')
        mais = int(input('\033[1;32mMostrar notas de qual aluno?\033[m \n\033[1;97m(Número negativo finaliza):\033[m '))
print('\033[1;32mFinalizando...\033[m')
sleep(2)
print('\033[1;97;32m{:•^50}\033[m'.format('VOLTE SEMPRE!'))
