c=float(input('\033[1;34mInforme a temperatura em °C:\033[m'))
f=9*c/5+32 #pela ordem de precedência,não precisa de parênteses.
print('\033[1;97mA temperatura de\033[m \033[1;36m{}°C\033[m \033[1;97mcorresponde a\033[m \033[1;35m{}°F\033[m\033[1;97m!\033[m'.format(c,f))
