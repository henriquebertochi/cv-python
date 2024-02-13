n = int(input('Digite um número: '))
soma = n
cont = 1
while n != 999:
    n = int(input('Digite um número: '))
    if n != 999:
        soma = soma + n
        cont += 1
print(f'Foram digitados {cont} números até acertar, a soma deles foi {soma}')