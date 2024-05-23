valores = []
continuar = 's'

while continuar == 's':
    valores.append(int(input('Digite um valor: ')))
    continuar = input('Quer continuar [s/n]: ').lower()
    if continuar not in 'sn':
        while continuar not in 'sn':
            continuar = input('Quer continuar [s/n]: ').lower()

print(f'Foram digitados os valores: {valores}')

par = valores[:]
imp = valores[:]

for v in valores:
    if v % 2 == 0:
        imp.remove(v)
    else:
        par.remove(v)

print(f'Valores PARES: {par}')
print(f'Valores IMPARES: {imp}')