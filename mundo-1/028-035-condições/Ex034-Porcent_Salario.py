'''Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
Para salários superiores a R$1250,00, calcule um aumento de 10%.
Para os inferiores ou iguais, o aumento é de 15%.'''

sal = float(input('Digite o seu salário (R$): '))
if sal > 1250:
    aum = (sal * 10) / 100
    novosal = sal + aum
else:
    aum = (sal * 15) / 100
    novosal = sal + aum
print(f'O seu sálario após o aumento será de R${novosal:.2f}')