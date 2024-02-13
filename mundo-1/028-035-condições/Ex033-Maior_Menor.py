'''Leia três números e mostre qual é o maior e qual é o menor.'''

n1 = int(input('Digite um número: '))
n2 = int(input('Digite um número: '))
n3 = int(input('Digite um número: '))
maior = 0
menor = 0
if n1 > n2 and n1 > n3:
    maior = n1
    if n2 > n3:
        menor = n3
    else:
        menor = n2
else:
    if n2 > n1 and n2 > n3:
        maior = n2
        if n1 > n3:
            menor = n3
        else:
            menor = n1
    else:
        if n1 > n2:
            maior = n3
            menor = n2
        else:
            maior = n3
            menor = n1
print(f'O maior número é {maior}')
print(f'O menor número é {menor}')