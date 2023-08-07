n1= float(input('\033[34mQuanto dinheiro você tem na carteira?\033[m')).__trunc__()
dol= n1 / 3.27
print('\033[1;97mBem, com essa quantia de\033[m {} \033[1;97mreais, você pode comprar\033[m {:.1f} \033[1;97mdólar(es)!\033[m'.format(n1,dol))