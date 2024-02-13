'''Crie um programa que leia duas notas de um aluno e calcule sua média,
mostrando uma mensagem no final, de acordo com a média atingida:
- Média abaixo de 5.0: REPROVADO
- Média entre 5.0 e 6.9: RECUPERAÇÃO
- Média 7.0 ou superior: APROVADO'''

n1 = float(input('Digite a sua primeira nota: [0/10] '))
n2 = float(input('Digite a sua segunda nota: [0/10] '))
if (n1 < 0 or n1 > 10) or (n2 < 0 or n2 > 10):
    print('Nota inválida!')
else:
    media = (n1 + n2) / 2
    print(f'A média ficou {media}')
    if media < 5:
        print('Reprovado!')
    elif media >= 5 and media < 7:
        print('Recuperação!')
    else:
        print('Aprovado!')