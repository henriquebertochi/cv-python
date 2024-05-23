dias = int(input('Quantos dias ficou com o carro? '))
km = float(input('Quantos Km foram rodados? '))
pdia = dias * 60
pkm = km * 0.15
p = pdia + pkm
print(f'O preço a se pagar é de R${p:.2}')