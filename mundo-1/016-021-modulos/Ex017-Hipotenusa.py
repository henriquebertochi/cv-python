import math

co = float(input('Digite o comprimento do cateto oposto: '))
ca = float(input('Digite o comprimento do cateto adjacente: '))
hi = ((co**2) + (ca**2)) ** (1/2)
hip = math.hypot(co, ca)
print(f'A hipotenusa vai medir {hi:.2f} -> **')
print(f'A hipotenusa vai medir {hip:.2f} -> math.hypot')