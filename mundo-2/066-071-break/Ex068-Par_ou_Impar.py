from random import randint

c = 0
while True:
    comp = randint(0, 11)
    escolha = input('Você quer Par ou Impar [P/I]? ').upper()
    if escolha != 'P' and escolha != 'I':
        print('Escolha inválida')
        break
    jog = int(input('Digite um número (0, 10): '))
    total = comp + jog
    if total % 2 == 0:
        print(f'Você jogou {jog} e o computador {comp}, total de {total} deu PAR')
        if escolha == 'P':
            print('Você VENCEU!')
            c += 1
        else:
            print(f'Você PERDEU, Jogador conseguiu {c} vitórias consecutivas!')
            break
    else:
        print(f'Você jogou {jog} e o computador {comp}, total de {total} deu IMPAR')
        if escolha == 'I':
            print('Você VENCEU')
            c += 1
        else:
            print(f'Você PERDEU, Jogador conseguiu {c} vitórias consecutivas!')
            break