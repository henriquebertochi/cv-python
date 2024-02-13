'''Leia as 3 medidas. Analise se pode formar um triângulo ou não'''

print('Insira os 3 lados do triângulo:')
lado1 = float(input('Lado 1 igual: '))
lado2 = float(input('Lado 2 igual: '))
lado3 = float(input('Lado 3 igual: '))
if (lado1 + lado2 > lado3) and (lado1 + lado3 > lado2) and (lado2 + lado3 > lado1):
    print('Pode formar um triângulo')
else:
    print('Não pode formar um triângulo')