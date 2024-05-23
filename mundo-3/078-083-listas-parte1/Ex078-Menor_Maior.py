valores = []
for c in range(0, 5):
    valores.append(int(input(f'Digite um número para a posição {c}: ')))
print(f'Os valores digitados foram: {valores}')

maior = max(valores)
print(f'O maior valor da lista é {maior} nas posições: ', end='')
for i, v in enumerate(valores):
    if v == maior:
        print(f'{i}... ', end='')
print('')

menor = min(valores)
print(f'O menor valor da lista é {menor} nas posições: ', end='')
for i, v in enumerate(valores):
    if v == menor:
        print(f'{i}... ', end='')
