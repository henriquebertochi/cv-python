preço = float(input('Digite o preço do produto: '))
desc = (preço * 5) / 100
novo = preço - desc
print(f'O preço com desconto de 5% é R${novo:.2f}')