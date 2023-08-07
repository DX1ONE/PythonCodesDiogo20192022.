from time import sleep
import emoji
from random import randint
print('{}{}{}'.format(emoji.emojize(':punho_levantado:', language='pt'),
                      emoji.emojize(':mão_levantada:', language='pt'),
                      emoji.emojize(':mão_em_v_de_vitória:', language='pt'))*10)
print('\033[1;30;43m                      JOKÊNPO                       \033[m')
print('{}{}{}'.format(emoji.emojize(':punho_levantado:', language='pt'),
                      emoji.emojize(':mão_levantada:', language='pt'),
                      emoji.emojize(':mão_em_v_de_vitória:', language='pt'))*10)
Pedra = ('{} - Pedra'.format(emoji.emojize(':punho_levantado:', language='pt')))
Papel = ('{} - Papel'.format(emoji.emojize(':mão_levantada:', language='pt')))
Tesoura = ('{} - Tesoura'.format(emoji.emojize(':mão_em_v_de_vitória:', language='pt')))
itens = ('Pedra', 'Papel', 'Tesoura')
pc = randint(0, 2)
print(' {}\033[1;97mEstá preparado para perder,pato?\033[m'.format(emoji.emojize(':quadrado_branco_médio_menor:',
                                                                                 language='pt')))
sleep(1)
print(' {}\033[1;97mEspero que sim,porque vamos começar!\033[m'.format(emoji.emojize(':quadrado_branco_médio_menor:',
                                                                                     language='pt')))
sleep(2)
print(' {}\033[1;33mSeu Turno\033[m{}'.format(emoji.emojize(':marca_de_seleção:', language='pt'),
                                              emoji.emojize(':marca_de_seleção:', language='pt')))
sleep(1)
print(''' {}\033[1;97mSuas opções:
[ 0 ] Pedra
[ 1 ] Papel 
[ 2 ] Tesoura\033[m'''.format(emoji.emojize(':quadrado_branco_médio_menor:', language='pt')))
sleep(2)
escolha = int(input('\033[1;97mSua Jogada:\033[m'))
sleep(1)
print(' {}\033[1;33mMeu Turno\033[m{}'.format(emoji.emojize(':marca_de_seleção:', language='pt'),
                                              emoji.emojize(':marca_de_seleção:', language='pt')))
sleep(2)
print(' {}\033[1;97mEu joguei:\033[m  \033[1;30;43m{}\033[m '.format(emoji.emojize(':quadrado_branco_médio_menor:',
                                                                                  language='pt'), itens[pc]))
sleep(2)
print('{:^40}'.format('\033[1;33mJO\033[m'))
sleep(1)
print('{:^40}'.format('\033[1;33m KEN\033[m'))
sleep(1)
print('{:^40}'.format('\033[1;33m    PÔ!!!\033[m'))
sleep(1)
print('\033[1;33m-=\033[m'*20)
print(' {}\033[1;97mComputador jogou:\033[m  \033[1;30;43m{}\033[m '.format(emoji.emojize(':quadrado_branco_médio_menor:',
                                                                                  language='pt'), itens[pc]))
print(' {}\033[1;97mVocê jogou:\033[m \033[1;30;43m{}\033[m'.format(emoji.emojize(':quadrado_branco_médio_menor:', language='pt'), itens[escolha]))
print('\033[1;33m-=\033[m'*20)
if pc == 0:
    if escolha == 0:
        print(' {}\033[1;97mEMPATE!\033[m'.format(emoji.emojize(':quadrado_branco_médio_menor:',
                                                                                language='pt')))
    elif escolha == 1:
        print(' {}\033[1;97mJOGADOR VENCE!\033[m'.format(emoji.emojize(':quadrado_branco_médio_menor:',
                                                                                   language='pt')))
    elif escolha == 2:
        print(' {}\033[1;97mCOMPUTADOR VENCE!\033[m'.format(emoji.emojize(':quadrado_branco_médio_menor:',
                                                                        language='pt')))

elif pc == 1:
    if escolha == 0:
        print(' {}\033[1;97mCOMPUTADOR VENCE!\033[m'.format(emoji.emojize(':quadrado_branco_médio_menor:',
                                                                        language='pt')))
    elif escolha == 1:
        print(' {}\033[1;97mEMPATE!\033[m'.format(emoji.emojize(':quadrado_branco_médio_menor:',
                                                                                language='pt')))
    elif escolha == 2:
        print(' {}\033[1;97mJOGADOR VENCE!\033[m'.format(emoji.emojize(':quadrado_branco_médio_menor:',
                                                                                   language='pt')))
elif pc == 2:
    if escolha == 0:
        print(' {}\033[1;97mJOGADOR VENCE!\033[m'.format(emoji.emojize(':quadrado_branco_médio_menor:',
                                                                                   language='pt')))
    elif escolha == 1:
        print(' {}\033[1;97mCOMPUTADOR VENCE!\033[m'.format(emoji.emojize(':quadrado_branco_médio_menor:',
                                                                        language='pt')))
    elif escolha == 2:
        print(' {}\033[1;97mEMPATE!\033[m'.format(emoji.emojize(':quadrado_branco_médio_menor:',
                                                                                language='pt')))
else:
    print('\033[1;31mVocê não escolheu uma das opções!\n Tente Novamente!\033[m')
print('')
print('\033[1;30;43m                       FIM                          \033[m')
