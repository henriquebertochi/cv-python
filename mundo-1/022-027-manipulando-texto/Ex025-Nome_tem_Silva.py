'''Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome'''

nome = str(input('Qual o seu nome? ')).strip() .upper()
tem = 'SILVA' in nome.split()
print(f'Seu nome possui Silva? {tem}')