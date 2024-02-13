soma_maior = 0
soma_menor = 0
for c in range(1, 8):
    ano = int(input('Qual o ano de nascimento? '))
    if 2023 - ano >= 18:
        soma_maior += 1
    else:
        soma_menor += 1
print(f'Das 7 pessoas, {soma_maior} pessoas já atingiram a maioridade')
print(f'E {soma_menor} já ainda são menores de idade')