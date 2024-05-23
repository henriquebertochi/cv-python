'''Faça um programa que leia o nome completo de uma pessoa, mostrando:
    a) O primeiro e o último nome separadamente'''

nome = str(input('Qual o seu nome? ')).strip() .title()
div = nome.split()
print(f'Seu primeiro nome é {div[0]}')
print(f'Seu último nome é {div[len(div)-1]}')