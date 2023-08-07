def tituloverde(msg):
    print('\033[1;97;42m~\033[m' * (len(msg) + 4))
    print(f'\033[1;97;42m  {msg}  \033[m')
    print('\033[1;97;42m~\033[m' * (len(msg) + 4))


def tituloazul(msg):
    print('\033[1;97;44m~\033[m' * (len(msg) + 4))
    print(f'\033[1;97;44m  {msg}  \033[m')
    print('\033[1;97;44m~\033[m' * (len(msg) + 4))


def titulovermelho(msg):
    print('\033[1;97;41m~\033[m' * (len(msg) + 4))
    print(f'\033[1;97;41m  {msg}  \033[m')
    print('\033[1;97;41m~\033[m' * (len(msg) + 4))


def pyhelp(txt):
    while True:
        if txt in'fim':
            titulovermelho('Até logo!')
            break
        tituloazul(f'Acessando o manual do comando {txt}')
        print(f'\033[1;30;107m ')
        help(txt)
        print(f'\033[m')
        tituloverde('Sistema de Ajuda PyHelp')
        pyhelp(str(input('Função ou Biblioteca> ')))




# Programa Principal
tituloverde('Sistema de Ajuda PyHelp')
pyhelp(str(input('Função ou Biblioteca> ')))


