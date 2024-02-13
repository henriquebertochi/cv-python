soma = 0
cont = 0
for c in range(1, 7):
    num = int(input('Digite um número inteiro: '))
    if num % 2 == 0:
        cont += 1
        soma += num
print(f'A soma dos {cont} números pares digitados é {soma}')