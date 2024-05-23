prim = int(input('Qual o primeiro termo da P.A? '))
raz = int(input('Qual a razão da P.A? '))
dec = prim + (10 - 1) * raz
for num in range(prim, dec, raz):
    print(num, end=' ')