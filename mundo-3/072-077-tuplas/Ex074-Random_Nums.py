from random import randint

sort = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))

print('Os valores sorteados foram: ', end='')
for num in sort:
    print(num, end=' ')
print('')

''' if sort[0] > sort[1] and sort[0] > sort[2] and sort[0] > sort[3] and sort[0] > sort[4]:
        print(f'O maior valor sorteado foi {sort[0]}') '''

print(f'O maior número sorteado foi {max(sort)}')
print(f'O menor número sorteado foi {min(sort)}')