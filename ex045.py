from random import randint
from time import sleep
jogo = ('Pedra', 'Papel', 'Tesoura')
pc = randint(1, 3)
print('''Escolha sua jogada
(1) Pedra
(2) Papel
(3) Tesoura''')
jogador = int(input('Qual é a sua jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!')
sleep(1)
print('=' * 20)
print('O pc jogou {}'.format(jogo[pc]))
print('Vc jogou {}'.format(jogo[jogador]))
print('=' * 20)
if pc == 1:
    if jogador == 1:
        print('Empate')
    elif jogador == 2:
        print('Vc ganhou')
    elif jogador == 3:
        print('O pc ganhou')
    else:
        print('Jogada inválida')
elif pc == 2:
    if jogador == 1:
        print('O pc ganhou')
    elif jogador == 2:
        print('Empate')
    elif jogador == 3:
        print('Vc ganhou')
    else:
        print('Jogada inválida')
elif pc == 3:
    if jogador == 1:
        print('Vc ganhou')
    elif jogador == 2:
        print('O pc ganhou')
    elif jogador == 3:
        print('Empate')
    else:
        print('Jogada inválida')

