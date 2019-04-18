sal = float(input('Digite seu salário R$: '))
if sal > 1250:
    print('Seu aumento será de 10% R${:.2f}'.format((sal * 0.1) + sal))
else:
    print('Seu aumento será de 15% R${:.2f}'.format((sal * 0.15) + sal))
