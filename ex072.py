extenso = ('zero', 'um', 'dois',
           'três', 'quatro', 'cinco',
           'seis', 'sete', 'oito',
           'nove', 'dez', 'onze',
           'doze', 'treze', 'quatorze',
           'quinze', 'dezesseis', 'dezessete',
           'dezoito', 'dezenove', 'vinte')
while True:
    n = int(input('Digite um número entre 0 e 20: '))
    if 0 <= n <= 20:
        print(f'Você digitou o número {extenso[n]}')
        denovo = str(input('Quer ir denovo? [S/N] ')).upper().strip()[0]
        if denovo in 'N':
            break
        elif denovo not in 'S':
            print('Opção Inválida! Tente Novamente.')
    elif 0 > n > 20:
        print('Tente Novamente!', end='')
/