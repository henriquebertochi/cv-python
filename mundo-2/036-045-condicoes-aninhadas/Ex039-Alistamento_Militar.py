'''Faça um programa que leia o ano de nascimento de um jovem
e informe, de acordo com a sua idade:
se ele ainda vai se alistar ao serviço militar,
se é a hora exata de se alistar,
ou se já passou do tempo do alistamento. Seu programa 
também deverá mostrar o tempo que falta ou que passou do prazo.'''

nasc = int(input('Digite o seu ano de nascimento: '))
atual = 2023
idade = atual - nasc
if idade < 18:
    faltam = 18 - idade
    print(f'Você ainda vai se alistar, faltam {faltam} anos')
elif idade == 18:
    print(f'Você tem que se alistar imediatamente!')
else:
    excedeu = idade - 18
    ano = atual - excedeu
    print(f'Você já deveria ter se alistado à {excedeu} anos, em {ano}')