dados = list()
pessoa = list()

while True:
    pessoa.append(input('Nome: ').capitalize())
    pessoa.append(float(input('Peso: ')))

    if len(dados) == 0:
        pesada = leve = pessoa[1]
    
    else:
        if pessoa[1] > pesada:
            pesada = pessoa[1]

        if pessoa[1] < leve:
            leve = pessoa[1]

    dados.append(pessoa[:])
    pessoa.clear()
    
    continuar = input('Quer continuar [s/n]: ').lower()
    if continuar not in 'sn':
        while continuar not in 'sn':
            continuar = input('Quer continuar [s/n]: ').lower()
    if continuar == 'n':
        break

print('='*30)

for p in dados:
    print(f'{p[0]} com {p[1]}kg') 

print('='*30)

print(f'Foram cadastradas {len(dados)} pessoas')

print('='*30)

print(f'A(s) pessoa(s) mais pesada(s) com {pesada}kg: ', end='')
for p in dados:
    if p[1] == pesada:
        print(f'{p[0]}', end=' - ')
print('')

print('='*30)

print(f'A(s) pessoa(s) mais leve(s) com {leve}kg: ', end='')
for p in dados:
    if p[1] == leve:
        print(f'{p[0]}', end=' ')
print('')