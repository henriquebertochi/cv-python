from time import sleep

jogadores = []
dados = {}
gols = []

while True:
    dados.clear()
    dados['nome'] = input('Qual o nome do jogador? ').capitalize()
    partidas = int(input(f'Quantas partidas {dados["nome"]} jogou? '))
    gols.clear()
    for p in range(1, (partidas)+1):
        gols.append(int(input(f'Quantos gols na partida {p}? ')))
    dados['gols'] = gols[:]
    dados['total'] = sum(gols)
    jogadores.append(dados.copy())
    resp = input('Quer continuar [S/N]? ').upper()[0]
    while resp not in 'SN':
        resp = input('Inválido. Quer continuar [S/N]? ').upper()[0 ]
    if resp == 'N':
        break

print('~'*40)

print('cod ', end='')
for i in dados.keys():
    print(f'{i:<15}', end='')
print()

print('~'*40)

for k, v in enumerate(jogadores):
    print(f'{k+1:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()

print('~'*40)

while True:
    busca = int(input('Mostrar dados de qual jogador [999 para]? '))
    if busca == 999:
        print('Finalizando...')
        sleep(1)
        break
    if busca > len(jogadores):
        print(f'ERRO, não existe jogador com código {busca}')
    else:
        print(f'Jogador {jogadores[busca-1]["nome"]}:')
        for i, g in enumerate(jogadores[busca-1]['gols']):
            print(f'--> No jogo {i+1} fez {g} gols')
    print('~'*40)