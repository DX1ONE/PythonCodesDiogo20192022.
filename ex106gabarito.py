from time import sleep

c = ('\033[m',          # 0 Sem cores
     '\033[1;97;41m',   # 1 Vermelho
     '\033[1;97;44m',   # 2 Azul
     '\033[1;30;107m',   # 3 Branco
     '\033[1;97;42m',    # 4 Verde
     );


def ajuda(com):
    titulo(f'Acessando o manual do comando \'{com}\'', 2)
    print(c[3], end='')
    help(com)
    print(c[0], end='')
    sleep(2)


def titulo(msg, cor=0):
    tam = len(msg) + 4
    print(c[cor], end='')
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)
    print(c[0], end='')
    sleep(1)

# Programa Principal
comando = ''
while True:
    titulo('Sistema de Ajuda PyHelp', 4)
    comando = str(input('Função ou Biblioteca> '))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
titulo('Até logo!', 1)