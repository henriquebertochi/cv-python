sex = input('Digite o seu sexo [M/F]: ').upper()
if sex == 'M' or sex == "F":
    print(f'Válido, {sex}')
else:
    while sex != 'M' and sex != 'F':
        print('Inválido, digite novamente!')
        sex = input('Digite o seu sexo [M/F]: ').upper()
    print(f'Válido, {sex}')