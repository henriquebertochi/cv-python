total = list()
aluno = list()
notas = list()

while True:
    nome = input('Qual o nome: ').capitalize()
    n1 = float(input('Nota 1: '))
    n2 = float(input('Nota 2: '))
    notas.append(n1)
    notas.append(n2)
    aluno.append(nome[:])
    aluno.append(notas[:])
    notas.clear()
    total.append(aluno[:])
    aluno.clear()
    resp = input('Quer continuar [s/n]? ').lower()
    while resp not in 'sn':
        resp = input('Quer continuar [s/n]? ').lower()
    if resp == 'n':
        break

for i, a in enumerate(total):
    print(f'{i}: {a[0]} - Média {((a[1][0]) + (a[1][1])) / 2}')

while True:
    qual = int(input('Mostrar as notas de qual aluno (999 interrompe)? '))
    if qual == 999:
        print('Finalizando..')
        break
    else:
        print(f'As notas de {total[qual][0]} são {total[qual][1][0]}, {total[qual][1][1]}')