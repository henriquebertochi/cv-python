while True:
    val = int(input('Digite o valor que vocÊ deseja saber a tabuada: '))
    if val < 0:
        print('Fim!')
        break
    mult = 1
    for num in range(1, 11):
        res = val * mult
        print(f'{val} X {mult} = {res}')
        mult += 1