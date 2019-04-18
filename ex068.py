from random import randint
print('=' * 20)
print('Jogue Par ou Impar')
print('=' * 20)
v = 0
while True:
    jogador = int(input('Digite seu valor: '))
    print('=' * 20)
    pc = randint(0, 11)
    total = jogador + pc
    tipo = ' '
    while tipo not in 'PI':
       tipo = str(input('Par ou Impar? [P/I]: ')).strip().upper()
       print('=' * 20)
    print(f'Vc jogou {jogador} e o pc {pc}, gerando um total de {total} ', end='')
    print('PAR' if total % 2 == 0 else 'IMPAR')
    print('=' * 48)
    if tipo == 'P':
        if total % 2 == 0:
            print('Vc ganhou! ')
            v += 1
        else:
            print('Vc perdeu!')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Vc ganhou!')
            v += 1
        else:
            print('Vc perdeu!')
            break
    print('Vamos jogar novamente...')
    print('=' * 24)
print(f'GAME OVER! Vc venceu {v} vezes')
