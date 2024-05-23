matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
somap = 0
soma3 = 0

for lin in range(0,3):
    for col in range(0, 3):
        matriz[lin][col] = int(input(f'Digite um valor para [{lin}, {col}]: '))

print('='*40)

for lin in range(0, 3):
    for col in range(0, 3):
        print(f'[{matriz[lin][col]:^6}]', end='')
        if matriz[lin][col] % 2 == 0:
            somap += matriz[lin][col]
    print('\n')

print('='*40)

print(f'A soma dos valores pares é {somap}')

print('='*40)

for lin in range(0,3):
    soma3 += matriz[lin][2]
print(f'A soma dos valores da terceira coluna é {soma3}')

print('='*40)

for col in range(0, 3):
    if col == 0:
        maior2 = matriz[1][col]
    elif matriz[1][col] > maior2:
        maior2 = matriz[1][col]
print(f'O maior valor da segunda linha é {maior2}')