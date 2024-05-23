nomebarato = ''
preçobarato = 100000000000000
mil = 0
total = 0

while True:
    nome = input('Qual o nome do produto? ').capitalize().strip()
    preço = int(input('Qual o preço do produto? R$'))
    total += preço
    if preço > 1000:
        mil += 1
    if preço < preçobarato:
        preçobarato = preço
        nomebarato = nome
    resp = input('Quer continuar [S/N]? ').upper().strip()
    while resp not in 'SN':
        print('Resposta inválida')
        resp = input('Quer continuar [S/N]? ').upper().strip()
    if resp == 'N':
        break
print(f'''Programa encerrado!
O total gasto na compra foi R${total:.2f}
{mil} prudutos custam mais de R$1000.00
{nomebarato} é o produto mais barato''')
