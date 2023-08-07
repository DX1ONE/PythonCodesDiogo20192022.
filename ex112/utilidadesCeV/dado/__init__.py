def leiaDinheiro(msg):
    """
    ->Função que recebe apenas valor monetário, sendo ela formatada ou não.
    :param msg: Valor desejado
    :return: Um número flutuante do valor digitado ou uma mensagem de erro caso não seja digitado um valor monetário.
    """
    valido = False
    while not valido:
        entrada = str(input(msg)).replace(',', '.').strip()
        if entrada.isalpha() or entrada == '':
            print(f'\033[1;31mERRO: \"{entrada}\" é um preço inválido!\033[m')
        else:
            valido = True
            return float(entrada)
