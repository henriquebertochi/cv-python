continuar = 's'
cont = 0
soma = 0
maior = 0
menor = 999999999999
while continuar == 's':
    num = int(input('Digite o número: '))
    soma = soma + num
    if num > maior:
        maior = num
    elif num < menor:
        menor = num
    cont += 1
    continuar = input('Você quer continuar digitando mais valores [s/n]? ').lower()
media = soma / cont
print(f'''A média entre todos os {cont} números digitados foi {media}
O maior número foi {maior}
E o menor número foi {menor}''')