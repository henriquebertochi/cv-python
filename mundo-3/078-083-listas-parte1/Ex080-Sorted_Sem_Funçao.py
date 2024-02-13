valores = []
for c in range(0, 5):
    v = int(input(f'Digite um valor: '))
    if c == 0 or v > valores[-1]:
        valores.append(v)
        print('-> Adiconado ao final da lista')
    else:
        pos = 0
        while pos < len(valores):
            if v <= valores[pos]:
                valores.insert(pos, v)
                print(f'-> Adicionado na posição {pos}')
                break
            pos += 1
print(f'Os valores digitados em ordem foram {valores}')