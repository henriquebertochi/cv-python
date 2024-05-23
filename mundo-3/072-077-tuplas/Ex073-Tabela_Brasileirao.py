tabela = ('Corinthians', 'Atlético-MG', 'Grêmio', 'São Paulo', 'Internacional', 'Sport', 'Santos', 'Cruzeiro', 'Palmeiras', 'Athletico-PR', 'Ponte Preta', 'Flamengo', 'Fluminense', 'Chapecoence', 'Coritiba', 'Figueirense', 'Avaí', 'Vasco', 'Goiás', 'Joinville')

cont = 1
print('--> Os 5 primeiros colocados são:')
for time in tabela[0: 5]:
    print(f'''{cont}° lugar: {time}''')
    cont += 1

print('=~'*18)

cont = 17
print('--> Os 4 últimos colocados são:')
for time in tabela[-4:]:
    print(f'''{cont}° lugar: {time}''')
    cont += 1

print('=~'*18)

print('--> Os times em ordem afabética:')
for time in sorted(tabela):
    print(time, end=' - ')
print('FIM!')

print('=~'*18)
print(f'Chapecoence está na {tabela.index("Chapecoence")+1}° posição!')