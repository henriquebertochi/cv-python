valores = []
continuar = 's'

while continuar == 's':
    valores.append(int(input('Digite um valor: ')))
    continuar = input('Quer continuar [s/n]: ').lower()
    if continuar not in 'sn':
        while continuar not in 'sn':
            continuar = input('Quer continuar [s/n]: ').lower()

print(f'Foram digitados {len(valores)} valores')

valores.sort(reverse=True)
print(f'Os valores em ordem decrescente são: {valores}')

if 5 in valores:
    print('Valor 5 está na lista')
else:
    print('Valor 5 não está na lista')