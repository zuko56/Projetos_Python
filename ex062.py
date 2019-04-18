print('=' * 13)
print('Gerador de PA')
print('=' * 13)
i = int(input('Digite o inicio da PA: '))
r = int(input('Digite a razão da PA: '))
termo = i
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print('{} > '.format(termo), end='')
        termo += r
        cont += 1
    print('Pausa')
    mais = int(input('Mais quantos termos deseja ver? '))
print('Foram mostrados {} termos da PA'.format(total))
print('Fim')



