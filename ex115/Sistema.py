from ex115.lib.Interface import *
from ex115.lib.Arquivo import *
from time import sleep

arq = 'Base de Nomes.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)
while True:
    resposta = menu(['Ver Pessoas Cadastradas', 'Cadastrar Novas Pessoas','Sair do Sistema'])
    if resposta == 1:
        # Opção de listar o conteúdo de um arquivo!
        lerArquivo(arq)
    elif resposta == 2:
        # Opção de cadastrar uma nova pessoa.
        cabeçalho('NOVO CADASTRO', 5,5)
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        cadastrar(arq,nome, idade)
    elif resposta == 3:
        cabeçalho('Saindo do Sistema...Até Logo!', 9)
        sleep(1)
        break
    else:
        print('\033[1;31mERRO: Digite uma opção válida!\033[m')
    sleep(2)