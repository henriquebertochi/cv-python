'''Faça um programa que leia uma frase e mostre:
    a) Quantas vezes aparece a letra "A"
    b) Em que posição ela aparece a primeira vez
    c) Em que posição ela aparece a última vez'''

frase = str(input('Digite uma frase: ')).strip() .upper()
vzs = frase.count('A')
print(f'A letra "A" aparece {vzs} vezes')
primeira = frase.find('A') + 1
print(f'A posição que ela aparece pela primeira vez é: {primeira}º')
ultima = frase.rfind('A') + 1
print(f'A posição que ela aparece pela última vez é: {ultima}º')