soma = 0
media = 0
idhvelho = 0
hvelho = ''
cont = 0
for c in range(0, 5):
    nome = input('Qual o nome da pessoa: ')
    idade = int(input('Qual a idade da pessoa: '))
    sexo = input('Qual o sexo da pessoa [m/f]: ')
    soma = soma + idade
    if sexo == 'm':
        if idade > idhvelho:
            hvelho = nome
            idhvelho = idade
        else:
            hvelho = hvelho
    if sexo == 'f':
        if idade < 20:
            cont += 1
media = soma / 5
print(f'A média das idades do grupo é {media}')
print(f'O nome do homem mais velho é {hvelho}')
print(f'{cont} mulheres tem menos de 20 anos')