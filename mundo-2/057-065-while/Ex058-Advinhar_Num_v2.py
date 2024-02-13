cont = 1
import random
num = random.randint(0, 10)
palp = int(input('Digite um número [0/10]: '))
if num == palp:
    print('Você venceu!')
else:
    while palp != num:
        print('Errado, tente novamente')
        palp = int(input('Digite um número [0/10]: '))
        cont += 1
    print(f'Acertou! Com um total de {cont} tentativas')        