vel = int(input('Digite a velocidade atual do carro: '))
if vel > 80:
    print('Multa! Dirija com cuidado')
    multa = (vel - 80) * 7
    print('O valor da multa será R${}'.format(multa))
else:
    print('Dirija com segurança')
