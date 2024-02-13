valores = []
continuar = 's'

while continuar == 's':
    v = int(input('Digite um valor: '))
    if v not in valores:
        valores.append(v)
        print('Valor adicionado á lista')
    else:
        print('Já adicionado, não irei repiti-lo')
    continuar = input('Quer continuar [s/n]: ').lower()
    if continuar not in 'sn':
        while continuar not in 'sn':
            continuar = input('Quer continuar [s/n]: ').lower()

print(f'Os valores em ordem crescente são: {sorted(valores)}')