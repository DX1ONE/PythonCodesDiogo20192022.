p1=float(input('\033[4;32mDigite o preço do produto:\033[m'))
p2= p1 * (5/100)
pf=p1 - p2
print('\033[1;30mO preço inicial do produto é de :\033[m {} \033[1;30mreais. \nO preço do produto com 5% de desconto é de:\033[m {} \033[1;30mreais.\033[m'.format(p1,pf))