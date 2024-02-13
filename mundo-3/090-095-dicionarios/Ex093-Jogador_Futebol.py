dados = {}
gols = []

dados['nome'] = input('Qual o nome do jogador? ').capitalize()

dados['partidas'] = int(input(f'Quantas partidas {dados["nome"]} jogou? '))

for p in range(1, (dados['partidas'])+1):
    gols.append(int(input(f'Quantos gols na partida {p}? ')))
dados['gols'] = gols

''' total = 0
for g in gols:
    total += g
dados['total'] = total '''

dados['total'] = sum(gols)

print('~'*30)

print(f'O jogador {dados["nome"]} jogou {dados["partidas"]} partidas')
for i, v in enumerate(dados['gols']):
    print(f'--> Na partida {i+1}, fez {v} gols')
print(f'Fez um total de {dados["total"]} gols!')