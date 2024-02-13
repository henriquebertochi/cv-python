from time import sleep
def linha():
    print('~'*50)
def contador(i, f, p):
    
    linha()
    print(f'Contagem de {i} até o {f} pulando {p} números')
    
    if p < 0:
        p *= -1
    if p < 0:
        p = 1

    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont} ', end='', flush=True)
            sleep(0.5)
            cont += p
        print('FIM')
    
    else:
        cont = i
        while cont >= f:
            print(f'{cont} ', end='', flush=True)
            sleep(0.5)
            cont -= p
        print('FIM!')

contador(1, 10, 1)
contador(10, 0, 2)
linha()
print('Personalize a contagem:')
ini = int(input('Início: '))
fim = int(input('Fim: '))
pas = int(input('Passo: '))
contador(ini, fim, pas)