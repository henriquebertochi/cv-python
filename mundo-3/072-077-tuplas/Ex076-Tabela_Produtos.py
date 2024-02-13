lista = ('Notebook', 3600,
         'Teclado', 220,
         'Mouse', 100,
         'MousePad', 90,
         'Incenso', 1.50,
         'Xícara', 9.75,
         'Café', 16.30)

print('='*50)
print(f'{"Tabela de Preços":^50}')
print('='*50)

prod = ''
valor = 0
for i in range(0, len(lista), 2):
    prod = lista[i]
    valor = lista[i + 1]
    print(f'{prod:.<37}   R${valor:>8.2f}')
print('='*50)
