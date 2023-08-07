info=input('\33[35mDigite algo:\033[m')
print(' \033[7;36m','É numérico?',info.isnumeric(),'\033[m \n',
'\033[7;36m','É um alpha-numérico?',info.isalnum(),'\033[m \n',
'\033[7;36m','É alfabético?',info.isalpha(),'\033[m \n',
'\033[7;36m','É um digito?',info.isdigit(),'\033[m \n',
'\033[7;36m','É ASCII?',info.isascii(),'\033[m \n',
'\033[7;36m','É decimal?',info.isdecimal(),'\033[m \n',
'\033[7;36m','É um identificador?',info.isidentifier(),'\033[m \n',
'\033[7;36m','Está em minúsculo?',info.islower(),'\033[m \n',
'\033[7;36m','É possível imprimir?',info.isprintable(),'\033[m \n',
'\033[7;36m','É um espaço?',info.isspace(),'\033[m \n',
'\033[7;36m','É um título?',info.istitle(),'\033[m \n',
'\033[7;36m','Está em maiúsculo?',info.isupper(),'\033[m')
