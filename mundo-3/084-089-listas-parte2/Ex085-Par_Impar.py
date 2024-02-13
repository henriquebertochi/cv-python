valores = [[], []]

for c in range(1, 8):
    n = int(input(f'Digite o {c}º número: '))
    if n % 2 == 0:
        valores[0].append(n)
    else:
        valores[1].append(n)
print('='*30)
print(f'Todos os números digitados foram: {valores}') 
print('='*30)
valores[0].sort()
print(f'PARES: {valores[0]}')
print('='*30)
valores[1].sort()
print(f'ÍMPARES: {valores[1]}')