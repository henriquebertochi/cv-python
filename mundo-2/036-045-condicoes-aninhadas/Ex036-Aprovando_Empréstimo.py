'''Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
    Pergunte o valor da casa
    o salário do comprador
    e em quantos anos ele vai pagar.
A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado'''


vcasa = float(input('Valor da casa: '))
sal = float(input('Salário: '))
anos = int(input('Quantos anos: '))
mensal = vcasa / (anos * 12)
if mensal > ((sal * 30) / 100):
    print('Empréstimo negado')
else:
    print('Empréstimo aceito')