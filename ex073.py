brasileirão = ('Corinthians', 'Palmeiras', 'Santos',
               'Grêmio', 'Cruzeiro', 'Flamengo',
               'Vasco da Gama', 'Chapecoense', 'Atlético-MG',
               'Botafogo', 'Athletico-PR', 'Bahia',
               'São Paulo', 'Fluminense', 'Sport Recife',
               'EC Vitória', 'Coritiba', 'Avaí',
               'Ponte Preta', 'Athlético-GO')
print('-=' * 50)
for t in brasileirão:
    print(f'{t}')
print('-=' * 50)
print(f'Os 5 primeiros: {brasileirão[:5]}')
print('-=' * 50)
print(f'Os últimos 4: {brasileirão[-4:]}')
print('-=' * 50)
print(f'{sorted(brasileirão)}')
print('-=' * 50)
print(f'O Chapecoense está na {brasileirão.index("Chapecoense") + 1}ª posição.')
print('-=' * 50)