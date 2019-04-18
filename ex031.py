viagem = int(input('Digite a distancia da viagem: '))
if viagem <= 200:
    preco = viagem * 0.50
else:
    preco = viagem * 0.45
print('O valor da passagem será R${:.2f}'.format(preco))
