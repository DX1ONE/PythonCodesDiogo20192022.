from datetime import date
dicionário = {}
dicionário['Nome'] = str(input('Nome: '))
ano = int(input('Ano de Nascimento: '))
atual = date.today().year
idade = atual - ano
dicionário['Idade'] = idade
dicionário['Ctps'] = int(input('Carteira de trabalho (0 não tem): '))
if dicionário['Ctps'] != 0:
    dicionário['Contratação'] = int(input('Ano de contratação: '))
    aposentadoria = (dicionário['Contratação'] - ano) + 35
    dicionário['Salário'] = float(input('Salário: R$'))
    dicionário['Aposentadoria'] = aposentadoria
print('—' * 30)
for v, k in dicionário.items():
    print(f'» {v}: {k}')
