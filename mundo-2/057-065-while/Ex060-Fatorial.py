num = int(input('Digite o número que você deseja saber o fatorial: '))
mult = num - 1
total = num
while mult > 1:
    total = total * mult
    mult -= 1
print(f'{num}! = {total}')