'''Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome "SANTO'''

cid = input('Digite o nome da sua cidade: ').strip() .title()
print(cid[:5] == 'Santo')