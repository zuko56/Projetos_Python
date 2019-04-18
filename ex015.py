km = int(input('Qual a quantidade de km percorridos? '))
dia = int(input('Quantos dias? '))
r = (60*dia) + (0.15*km)
print('Somando os custos o valor a pagar será R${:.2f}'.format(r))