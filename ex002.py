
cores = {'pretoebranco':'\033[1;30;107m','vermelho':'\033[31;40m','limpa':'\033[m'}
n1=int(input('\033[97mDigite um número:'))
n2=int(input('\033[97mDigite outro número:'))
s= n1 + n2
#print('A soma entre',n1,'e',n2,'vale {}'.format(s)) tem muitas vírgulas,para isto foi impregado o .format
print('{}A some entre{} {}{}{} {}e{} {}{}{} {}vale{} {}{}{}'.format(cores['pretoebranco'], cores['limpa'], cores['vermelho'], n1, cores['limpa'], cores['pretoebranco'], cores['limpa'], cores['vermelho'], n2, cores['limpa'], cores['pretoebranco'], cores['limpa'],cores['vermelho'], s, cores['limpa']))