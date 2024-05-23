num = int(input('Quantos números da sequência de Finonacci você deseja? '))
n1 = 0
n2 = 1
fib = ''
print(n1, n2, end='')
cont = 3
while cont <= num:
    fib = n1 + n2
    print('', fib, end='')
    n1 = n2
    n2 = fib
    cont += 1
print(' Fim!')