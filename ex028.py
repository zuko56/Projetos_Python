from random import randint
pc = randint(0, 10)
print('Tente advinhar um número entre 0 a 10')
acertou = False
cont = 0
while not acertou:
    jog = int(input('Digite seu palpite: '))
    cont += 1
    if jog == pc:
        acertou = True
    else:
        if jog < pc:
            print('É um valor maior...')
        elif jog > pc:
            print('É um valor menor...')
print('Vc acertou! com {} tentativas'.format(cont))
