soma = 0
cont = 0
for num in range(1, 501):
    if (num % 2 != 0) and (num % 3 == 0):
        cont += 1
        soma = soma + num
print(f'A soma dos {cont} valores válidos é {soma}')