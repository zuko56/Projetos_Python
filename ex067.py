while True:
    n = int(input('Digite um número e veja sua tabuada: '))
    if n < 0:
        print('Finalizando o programa...')
        break
    for t in range(1, 11):
        print(f'{n} X {t:2} = {n*t}')
