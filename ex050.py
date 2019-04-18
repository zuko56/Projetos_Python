s = 0
cont = 0
for c in range(1, 7):
    n = int(input('Digite um numero inteiro: '))
    if n % 2 == 0:
        s += n
        cont += 1
print('Vc informou {} números pares e a soma é {}'.format(cont, s))
