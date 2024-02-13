'''Escreva um programa que leia a velocidade de um carro.
Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
A multa vai custar R$7,00 por cada Km acima do limite.'''

velo = int(input('Qual a velocidade que seu carro está (Km/h) ? '))
if velo > 80:
    multa = (velo - 80) * 7
    print(f'Você está acima do limite permitido! Deve pagar uma multa de R${multa}')
else:
    print('Você está no limite permitido!')