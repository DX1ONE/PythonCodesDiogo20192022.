def leiaInt():
   while True:
       try:
            n = str(input('Digite um Inteiro:')).strip()
            if n.isalpha() or n == float(n) or n == '':
                print('\033[1;31mERRO: pof favor, digite um número inteiro válido.\033[m')
            else:
                n = int(n)
                break
       except ValueError:
            print(f'Desculpe, tivemos um erro com o valor digitado')
       else:
            return n
       finally:
            print('<---Volte Sempre--->'.center(30))


while True:
    m = str(input('Digite um Real: ')).strip()
    if m.isalpha or m == int(m) or m == '':
        print('\033[1;31mERRO: por favor, digite um número real válido.\033[m')
    else:
        m = float(m)
        break
print(f'O inteiro digitado foi {n} e o real foi {m}.')



leiaInt()
