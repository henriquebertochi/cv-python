'''Elabore um programa que calcule o valor a ser pago por um produto,
considerando o seu preço normal e condição de pagamento:
- à vista dinheiro/cheque: 10% de desconto
- à vista no cartão: 5% de desconto
- em até 2x no cartão: preço formal
- 3x ou mais no cartão: 20% de juros'''

prod = float(input('Digite o preço da compra: R$'))
print('''Escolha uma das opções de pagamento:
[ 1 ] À vista em dinheiro/cheque: 10% de desconto
[ 2 ] À vista no cartão: 5% de desconto
[ 3 ] Em até 2x no cartão: preço formal
[ 4 ] 3x ou mais no cartão: 20% de juros''')
opção = int(input('Sua opção: '))
if opção == 1:
    desc = (prod * 10) / 100
    preço = prod - desc
    print(f'A compra de R${prod:.2f} pagando à vista em dinheiro/cheque fica {preço:.2f}')
elif opção == 2:
    desc = (prod * 5) / 100
    preço = prod - desc
    print(f'A compra de R${prod:.2f} pagando à vista no cartão fica {preço:.2f}')
elif opção == 3:
    cart2 = prod / 2
    print(f'A compra parcelada no cartão em 2x, fica 2 parcelas de R${cart2:.2f} SEM JUROS!')
elif opção == 4:
    vzs = int(input('Quantas parcelas? '))
    juros = (prod * 20) / 100
    preço = prod + juros
    cart = preço / vzs
    print(f'Sua compra será parcelada em {vzs}x de R${cart:.2f} COM JUROS')
    print(f'Sua compra de R${prod:.2f} vai custar R${preço:.2f} no final')
else:
    print('Opção inválida')