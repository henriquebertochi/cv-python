'''Leia o nome completo e mostre:
    a) O nome com todas as letras maíúsculas
    b) O nome com todas minúsculas
    c) Quantas letras ao todo(sem considerar espaços)
    d) Quantas letras tem o primeiro nome'''

nome = str(input('Digite o seu nome completo: ')).strip() .title()
print(f'Seu nome em maiúsculas é {nome.upper()}')
print(f'Seu nome em minúsculas é {nome.lower()}')
semespaço = len(nome) - nome.count(' ')
print(f'Seu nome tem ao todo {semespaço} letras')
separado = nome.split()
print(f'Seu primeiro nome é {separado[0]} e ele tem {len(separado[0])} letras')