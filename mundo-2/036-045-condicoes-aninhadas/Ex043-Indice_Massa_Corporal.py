'''Desenvolva uma lógica que leia o peso e a altura de uma pessoa,
calcule seu Índice de Massa Corporal (IMC)
mostre seu status de acordo com a tabela abaixo:
- IMC abaixo de 18,5: Abaixo do Peso
- Entre 18,5 e 25: Peso Ideal
- 25 até 30: Sobrepeso
- 30 até 40: Obesidade
- Acima de 40: Obesidade Mórbida'''

peso = float(input('Digite o seu peso em kg: '))
alt = float(input('Digite a sua altura em metros: '))
imc = peso / (alt**2)
print(f'O seu IMC é: {imc:.1f}')
if imc < 18.5:
    print('Está abaxio do peso')
elif imc >= 18.5 and imc < 25:
    print('Está com o peso ideal')
elif imc >= 25 and imc < 30:
    print('Está sobrepeso')
elif imc >= 30 and imc < 40:
    print('Está obeso')
else:
    print('Está com obesidade mórbida')