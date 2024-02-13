prim = int(input('Qual o primeiro termo da P.A? '))
raz = int(input('Qual a razão da P.A? '))
cont = 0
num = prim
print(prim, end=' ')
while cont < 9:
    num = num + raz
    print(num, end=' ')
    cont += 1