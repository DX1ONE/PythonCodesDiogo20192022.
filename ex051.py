print('\033[1;97m=\033[m'*30)
print('\033[1;30;107m{:^30}\033[m'.format('10 TERMOS DE UMA PA'))
print('\033[1;97m=\033[m'*30)


t = int(input('\033[1;97mQual o primeiro termo da PA?\033[m'))
r = int(input('\033[1;97mQual é a razão?\033[m'))
decimo = t + (10 - 1) * r
for c in range(t, decimo + r, r):
    print('\033[1;97m {} \033[m'.format(c), end='\033[1;97m⇢\033[m ')
print('\033[1;30;107mACABOU\033[m')