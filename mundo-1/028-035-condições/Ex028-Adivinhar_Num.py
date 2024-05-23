'''Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5.
peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
O programa deverá escrever na tela se o usuário venceu ou perdeu.'''

import random
num = random.randint(0, 5)
palp = int(input('Digite um número [0/5]: '))
if num == palp:
    print('Você venceu!')
else:
    print('Você perdeu!')