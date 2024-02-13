def linha():
    print('~'*35)

def maior(lst):
    linha()
    for n in lst:
        print(n, end=' - ')
    print('Fim')
    print(f'Foram passados {len(lst)} valores ao todo')
    print(f'O maior valor informado foi {max(lst)}')
    linha()

lst = []
while True:
    num = int(input('Informe um número: '))
    lst.append(num)
    resp = input('Quer continuar [S/N]? ').upper()[0]
    while resp not in 'SN':
        resp = input('Inválido. Quer continuar [S/N]? ').upper()[0 ]
    if resp == 'N':
        break
maior(lst)