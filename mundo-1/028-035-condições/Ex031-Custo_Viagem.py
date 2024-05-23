'''Desenvolva um programa que pergunte a distância de uma viagem em Km.
Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km
e R$0,45 parta viagens mais longas.'''

dist = int(input('Digite a distânica da viagem (Km): '))
if dist <= 200:
    preço = 0.5 * dist
    print(f'O preço da passagem será R${preço:.2f}')
else:
    preço = 0.45 * dist
    print(f'O preço da passagem será R${preço:.2f}')