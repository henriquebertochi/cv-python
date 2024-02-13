from random import randint
from time import sleep

sorteados = list()
jogo = list()

quantos = int(input('Quantos jogos você deseja sortear? '))
print(f'-> Sorteando {quantos} jogos:')
for j in range(1, quantos+1):
    for n in range(1, 7):
        valor = randint(1, 60)
        while valor in jogo:
            valor = randint(1, 60)
        jogo.append(valor)
    sorteados.append(jogo[:])
    jogo.clear()

for i, j in enumerate(sorteados):
    print(f'Jogo {i+1}: {j}')
    sleep(1)
print('Boa sorte!')