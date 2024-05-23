import math
ang = float(input('Digite o ângulo: '))
sen = math.sin(math.radians(ang))
cos = math.cos(math.radians(ang))
tg = math.tan(math.radians(ang))
print(f'O seno de {ang}° é {sen:.2f}')
print(f'O cosseno de {ang}° é {cos:.2f}')
print(f'A tangente de {ang}° é {tg:.2f}')