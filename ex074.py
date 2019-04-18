from random import randint
sorteio = (randint(1, 11), randint(1, 11), randint(1, 11), randint(1, 11), randint(1, 11))
print(f'Os valores sorteados foram {sorteio}')
print(f'O maior valor sorteado foi {max(sorteio)}')
print(f'O menor valor sorteado foi {min(sorteio)}')

