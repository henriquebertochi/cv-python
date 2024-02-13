maior = 0
menor = 999999
for c in range(1, 6):
    peso = int(input('Digite o peso: '))
    if peso > maior:
        maior = peso
    elif peso < menor:
        menor = peso
print(f'Das 5 pessoas, o maior peso foi {maior} e o menor peso foi {menor}')