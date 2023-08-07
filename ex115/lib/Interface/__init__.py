def leiaInt(msg):
    while True:

        try:
            n = int(input(msg))

        except (ValueError, TypeError):
            print('\033[1;31mERRO: por favor, digite um número inteiro \nválido.\033[m')
            continue

        except KeyboardInterrupt:
            print('\n\033[1;31mO usuário preferiu não digitar esse valor.\033[m')
            return 0

        else:
            return n

def linha(tam = 42):
    return ('—' * tam)


cores = ('\033[m',      # 0 - Limpa
         '\033[1;30m',  # 1 - Preto
         '\033[1;31m',  # 2 - Vermelho
         '\033[1;32m',  # 3 - Verde
         '\033[1;33m',  # 4 - Amarelo
         '\033[1;34m',  # 5 - Azul
         '\033[1;35m',  # 6 - Roxo
         '\033[1;36m',  # 7 - Ciano
         '\033[1;37m',  # 8 - Cinza
         '\033[1;97m')  # 9 - Branco


def cabeçalho(txt, cor=0, limpa=0):
    cor = cores[cor]
    limpa = cores[limpa]
    print(cor, linha(), cor)
    print(cor, txt.center(42), cor)
    print(cor, linha(), cor, limpa)


def menu(lista):
    cabeçalho('MENU PRINCIPAL', 5)
    c = 1
    for item in lista:
        print(f'\033[1;34m{c}\033[m - \033[1;97m{item}\033[m')
        c += 1
    print('\033[1;34m', linha(), '\033[m')
    opc = leiaInt('\033[1;34mSua Opção: \033[m')
    return opc