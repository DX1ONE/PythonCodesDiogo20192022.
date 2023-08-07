def leiaInt(n):
    """
    ->Lê apenas número inteiro e imprime uma string dizendo o número digitado.
    :param n:Um número inteiro
    :return:Uma string dizendo o número que foi digitado.
    """
    while True:
        n = str(input('Digite um número: '))
        if not n.isnumeric():
            print(f'\033[1;31mERRO! Digite um número inteiro válido.\033[m')
        else:
            return n
            break

# Programa Principal
n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}')
