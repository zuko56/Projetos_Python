casa = float(input('Digite o valor da casa R$: '))
sal = float(input('Digite seu salário R$: '))
ano = int(input('Em quantos anos deseja pagar: '))
pres = casa / (ano * 12)
if pres <= sal * 0.3:
    print('Emprestimo aceito, o valor da prestação mensal será de {:.2f}'.format(pres))
else:
    print('Seu empréstimo foi negado, o valor da prestação seria de {:.2f}'.format(pres))
