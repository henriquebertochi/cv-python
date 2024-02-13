prim = int(input('Qual o primeiro termo da P.A? '))
raz = int(input('Qual a razão da P.A? '))
cont = 0
total = 0
num = prim
mais = 10
while mais != 0:
    total = total + mais
    while cont < total:
        print(num, end=' ')
        num = num + raz
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print('FIM!')