'''i = int(input('Digite o inicio da PA: '))
r = int(input('Digite a razão da PA: '))
decimo = i + (10 - 1) * r
for c in range(i, decimo + r, r):
    print(c, end=' ')
print('\nOs primeiros 10 termos da PA são esses acima')'''
print('=' * 13)
print('Gerador de PA')
print('=' * 13)
i = int(input('Digite o inicio da PA: '))
r = int(input('Digite a razão da PA: '))
termo = i
cont = 1
while cont <= 10:
    print('{} > '.format(termo), end='')
    termo += r
    cont += 1
print('Fim')



