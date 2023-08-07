from datetime import date
totmaior = 0
totmenor = 0
for c in range(1, 8):
    nascimento = int(input('Em que ano a {}ª pessoa nasceu:'.format(c)))
    atual = date.today().year
    if atual - nascimento < 18:
        totmenor += 1
    elif atual - nascimento >= 18:
        totmaior += 1
print('Entre estas pessoas, {} já são maiores de idade! e {} são menores.'.format(totmaior, totmenor))
