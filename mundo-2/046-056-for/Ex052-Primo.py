num = int(input('Digite um número: '))
if num < 2:
    print('Não é primo')
else:
    divisores = 2
    divisor = 2
    while divisor <= num // 2:
        if num % divisor == 0:
            divisores += 1
        divisor += 1
if divisores > 2:
    print('Não é primo')
else:
    print('É primo')