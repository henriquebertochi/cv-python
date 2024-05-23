'''Refaça o DESAFIO 035 dos triângulos,
acrescentando o recurso de mostrar que tipo de triângulo será formado:
- EQUILÁTERO: todos os lados iguais
- ISÓSCELES: dois lados iguais, um diferente
- ESCALENO: todos os lados diferentes'''

print('Insira os 3 lados do triângulo:')
lado1 = float(input('Lado 1 igual: '))
lado2 = float(input('Lado 2 igual: '))
lado3 = float(input('Lado 3 igual: '))
if (lado1 + lado2 > lado3) and (lado1 + lado3 > lado2) and (lado2 + lado3 > lado1):
    print('Pode formar um triângulo')
    if lado1 == lado2 and lado1 == lado3:
        print('Triângulo EQUILÁTERO')
    elif lado1 != lado2 and lado1 != lado3 and lado2 != lado3:
        print('Triângulo ESCALENO')
    else:
        print('Triângulo ISÓSCELES')
else:
    print('Não pode formar um triângulo')