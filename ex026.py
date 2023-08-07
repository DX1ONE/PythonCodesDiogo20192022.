f = str(input('\033[1;97mDigite uma frase:\033[m')).lower().strip()
apa = f.count('a')
n1 = f.strip().find('a') + 1
n2 = f.rfind('a') + 1
print('A letra a aparece \033[1;30m{}\033[m vezes '
      '\nsua primeira aparição foi no caractere \033[1;30m{}\033[m '
      '\ne a última aparição foi no caractere \033[1;30m{}\033[m.'.format(apa, n1, n2))
