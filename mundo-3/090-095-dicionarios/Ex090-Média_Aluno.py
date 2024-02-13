aluno = {}
aluno['nome'] = input('Nome: ').capitalize()
aluno['media'] = float(input('Média: '))
if aluno['media'] >= 7:
    aluno['sit'] = 'Aprovado!'
else:
    aluno['sit'] = 'Reprovado'
print('='*15)
print(f'Nome é {aluno["nome"]}')
print(f'Média é {(aluno["media"]):.1f}')
print(f'Situação é {aluno["sit"]}')