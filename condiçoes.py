n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1+n2)/2
print('Sua média é {:.1f}'.format(m))
print('Está na média' if m >= 6.0 else 'Está abaixo da média')
