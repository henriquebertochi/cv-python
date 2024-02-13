from random import randint
from time import sleep
from operator import itemgetter

dados = {'Jogador1': randint(1, 6),
         'Jogador2': randint(1, 6),
         'Jogador3': randint(1, 6),
         'Jogador4': randint(1, 6)}
print('\033[1;35mDados sorteados:\033[m')
for k, v in dados.items():
    print(f'--> O {k} tirou {v}')
    sleep(0.5)

print('~'*30)

ordem = sorted(dados.items(), key=(itemgetter(1)), reverse=True)
print('\033[1;33 mRanking:\033[m')
for i, v in enumerate(ordem):
    print(f'{i+1}º Lugar: {v[0]} com {v[1]}')