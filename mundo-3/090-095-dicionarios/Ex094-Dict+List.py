grupo = []
pessoa = {}
soma = media = 0
while True:
    pessoa.clear()
    pessoa['nome'] = input('Nome: ').capitalize()
    while True:
        pessoa['sexo'] = input('Sexo [M/F]: ').upper()
        if pessoa['sexo'] in 'MF':
            break
        print('Erro!')
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    grupo.append(pessoa.copy())
    resp = input('Quer continuar [S/N]? ').upper()
    while resp not in 'SN':
        resp = input('Inválido. Quer continuar [S/N]? ').upper()
    if resp == 'N':
        break

print('~'*30)

print(f'Foram cadastradas {len(grupo)} pessoas')

media = soma / len(grupo)
print(f'A média de idade é de {media:.2f} anos')

print(f'As mulheres cadastradas foram: ', end='')
for p in grupo:
    if p['sexo'] == 'F':
        print(f'{p["nome"]}', end=' - ')
print()

print(f'As pessoas com idade acima da média são: ', end='')
for p in grupo:
    if p['idade'] > media:
        print(f'{p["nome"]} com {p["idade"]} anos', end=' - ')