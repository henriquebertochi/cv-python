palavras = ('i', 'guess', 'i', 'am', 'afraid', 'there', 'is', 'nothing', 'to', 'be', 'afraid', 'mister', 'morgan', 'take', 'a', 'gamble', 'that', 'love', 'exists')

for p in palavras:
    print(f'\n{p.upper()}: ', end='')
    for letra in p:
        if letra.upper() in 'AEIOU':
            print(f'{letra}', end=' ')