exp = input('Digite a expressão: ')
pilha = []

for d in exp:
    if d == '(':
        pilha.append('(')
    elif d == ')':
        pilha.pop()
    else:
        pilha.append(')')
        break

if len(pilha) == 0:
    print('Expressão Válida')
else:
    print('Expressão Inválida')