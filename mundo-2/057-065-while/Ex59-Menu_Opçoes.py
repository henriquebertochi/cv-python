opc = 4
while opc == 4:
    n1 = int(input('Digite um valor: '))
    n2 = int(input('Digite outro valor: '))
    print('''Opções:
    [ 1 ] Somar
    [ 2 ] Multiplicar
    [ 3 ] Maior
    [ 4 ] Novos números
    [ 5 ] Sair do programa''')
    opc = int(input('Qual foi a opção desejada? '))

if opc == 1:
    soma = n1 + n2
    print(f'A soma dos dois valores é {soma}')

elif opc == 2:
    mult = n1 * n2
    print(f'A multiplicação dos dois valores é {mult}')

elif opc == 3:
    if n1 > n2:
        print(f'O primeiro valor ({n1}) é o maior')
    elif n2 > n1:
        print(f'O segundo valor ({n2}) é o maior')
    else:
        print(f'Os dois valores são iguais, não existe maior')

elif opc == 5:
    print('OK, tchau!')

else:
    print('Opção inexistente!')