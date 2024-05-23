mais18 = 0
homens = 0
mulhe20 = 0

while True:
    idade = int(input('Qual a idade: '))
    sexo = input('Qual o sexo [M/F]: ').upper()
    if sexo != 'M' and sexo != 'F':
        print('Sexo inválido')
        break
    if idade > 18:
        mais18 += 1
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade < 20:
        mulhe20 += 1
    continuar = input('Deseja continuar [S/N]: ').upper()
    if continuar == 'N':
        print(f'''Programa parado!
              {mais18} pessoas tem mais de 18 anos
              {homens} homens foram cadastrados
              {mulhe20} mulheres tem menos de 20 anos''')
        break