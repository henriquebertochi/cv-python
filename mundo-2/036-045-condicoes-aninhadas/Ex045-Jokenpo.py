'''Crie um programa que faça o computador jogar Jokenpô com você'''

import random

print('''Suas opções:
[ 1 ] Pedra
[ 2 ] Papel
[ 3 ] Tesoura''')
jog = int(input('Qual sua jogada? '))
if jog >= 1 and jog <= 3:
    if jog == 1:
        print('Jogador jogou Pedra')
    elif jog == 2:
        print('Jogador jogou Papel')
    else:
        print('Jogador jogou Tesoura')
    comp = random.randint(1, 3)
    if comp == 1:
        print('Computador jogou Pedra')
    elif comp == 2:
        print('Computador jogou Papel')
    else:
        print('Computador jogou Tesoura')
    if jog == comp:
        print('Empatou')
    else:
        if comp == 1:
            if jog == 2:
                print('Jogador VENCEU')
            else:
                print('Computador Venceu')
        elif comp == 2:
            if jog == 1:
                print('Computador VENCEU')
            else:
                print('Jogador Venceu')
        elif comp == 3:
            if jog == 1:
                print('Jogador VENCEU')
            else:
                print('Computador VENCEU')
        else:
            print('Jogada inválida')
else:
    print('Jogada inválida')