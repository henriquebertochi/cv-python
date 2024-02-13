dados = {}

nome = input('Qual o seu nome? ').capitalize()
dados['nome'] = nome

ano = int(input('Qual seu ano de nascimento? '))
idade = 2023 - ano
dados['idade'] = idade

ctps = int(input('Qual o número da Carteira de Trabalho (0 não tem)? '))
if ctps == 0:
    dados['ctps'] = ctps
    print('~'*20)
    for k, v in dados.items():
        print(f'{k}: {v}')

else:
    dados['ctps'] = ctps

    contrataçao = int(input('Qual foi o ano de contratação? '))
    dados['contratação'] = contrataçao

    sal = float(input('Qual seu salário? R$'))
    dados['salário'] = sal

    apos = (idade - (2023-contrataçao))+35
    dados['aposentadoria'] = apos

print('~'*20)
for k, v in dados.items():
    print(f'{k}: {v}')