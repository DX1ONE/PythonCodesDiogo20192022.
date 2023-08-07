import urllib
import urllib.request

try:
    site = urllib.request.urlopen('https://www.piadas.com.br')
except:
    print('\033[1;31mO site Piadas não está acessivel no momento.\033[m')
else:
    print('\033[1;32mConsegui acessar o site Piadas com Sucesso!\033[m')
    print(site.read())