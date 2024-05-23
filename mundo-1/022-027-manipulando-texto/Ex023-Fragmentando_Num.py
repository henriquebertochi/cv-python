'''Ler um número de 0 a 9999 e mostrar cada digito separado'''

num = int(input('Digite um número [0/9999]: '))
if num < 10000:
    u = (num // 1) % 10
    d = (num // 10) % 10
    c = (num // 100) % 10
    m = (num // 1000) % 10
    print(f'Unidade: {u}')
    print(f'Dezena: {d}')
    print(f'Centena: {c}')
    print(f'Milhar: {m}')
else:
    print('Erro! O número não esta entre 0 e 9999')