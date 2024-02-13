entrada = input('Digite uma frase: ').strip()
inv = ""
cont = -1
while cont >= len(entrada)*-1:
    inv = inv + entrada[cont]
    cont -= 1
print(inv)
if inv == entrada:
    print('É um palindromo')
else: 
    print('Não é um palindromo')