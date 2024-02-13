'''Leia um ano e diga se é bissexto.
Se o usuário digitar 0, se refere ao ano atual (2023)'''

atual = 2023
ano = int(input('Digite o ano (Se quer saber sobre o ano atual, digite 0): '))
if ano == 0:
    ano = atual
else:
    if ano % 4 == 0:
        if ano % 100 == 0:
            if ano % 400 == 0:
                print(f'O ano de {ano} é bissexto')
            else:
                print(f'O ano de {ano} não é bissexto')
        else:
            print(f'O ano de {ano} é bissexto')
    else:
        print(f'O ano de {ano} não é bissexto')