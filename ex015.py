km=float(input('\033[7;31mQuantos quilômetros foram rodados com o carro ?\033[m'))
dias=int(input('\033[7;33mPor quantos dias o carro foi alugado?\033[m'))
pago= (km * 0.15) + (dias * 60)
print('\033[7;32mO preço a pagar é de {} reais.\033[m'.format(pago))