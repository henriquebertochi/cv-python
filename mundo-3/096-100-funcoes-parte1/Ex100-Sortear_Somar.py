from random import randint

def linha():
    print('~'*60)

def sorteio(lista):
    linha()
    print('Sorteando 5 valores da lista: ', end='')
    for cont in range(0, 5):
        n = randint(1, 10)
        lista.append(n)
        print(f'{n}', end=' - ')
    print('Fim')
    linha()

def somapar(lista):
    soma = 0
    for v in lista:
        if v % 2 == 0:
            soma += v
    print(f'Somando os valores pares dos sorteados temos {soma}')
    linha()

'''-'''

numeros = list()
sorteio(numeros)
somapar(numeros)