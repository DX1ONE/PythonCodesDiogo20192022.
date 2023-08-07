def leiaInt(msg):
    while True:

        try:
            n = int(input(msg))

        except (ValueError, TypeError):
            print('\033[1;31mERRO: por favor, digite um número inteiro válido.\033[m')
            continue

        except KeyboardInterrupt:
            print('\n\033[1;31mO usuário preferiu não digitar esse valor.\033[m')
            return 0

        else:
            return n


def leiaFloat(msg):
    while True:

        try:
            n = float(input(msg))

        except (ValueError, TypeError):
            print(f'\033[1;31mERRO: por favor, digite um número real válido.\033[m')
            continue

        except KeyboardInterrupt:
            print('\n\033[1;31mUsuário preferiu não digitar esse valor.\033[m')
            return 0

        else:
            return n


n1 = leiaInt('\033[1;97mDigite um Inteiro: \033[m')
n2 = leiaFloat('\033[1;97mDigite um Real: \033[m')
print(f'\033[1;97mO valor inteiro digitado foi {n1} e o real foi {n2}\033[m ')