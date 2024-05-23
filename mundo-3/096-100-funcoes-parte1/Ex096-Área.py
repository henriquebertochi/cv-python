def linha():
    print('~'*20)

def area(l, c):
    a = l * c
    print(f'A largura de um terreno {l} x {c} é de {a}m²')

l = float(input('Largura (m): '))
c = float(input('Comprimento (m): '))
linha()
area(l, c)