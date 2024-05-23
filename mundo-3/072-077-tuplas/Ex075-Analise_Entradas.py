numeros = (int(input('Digite um número: ')), int(input('Digite mais um número: ')), int(input('Digite outro número: ')), int(input('Digite o último número: ')))

print('Você digitou os valores: ', end='')
for n in numeros:
    print(n, end=' ')
print('')

print('=~'*15)

print(f'O número 9 apareceu {numeros.count(9)} vezes')

print('=~'*15)

if 3 in numeros:
    print(f'O número 3 foi digitado na {numeros.index(3)+1}ª posição')
else:
    print('O número 3 não foi digitado em nenhuma posição')

print('=~'*15)

print('Os valores pares digitados foram: ', end='')
for n in numeros:
    if n % 2 == 0:
        print(n, end=' ')