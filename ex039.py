from datetime import date
atual = date.today().year
nasc = int(input('Digite o ano de nascimento: '))
idade = atual - nasc
print('Quem nasceu em {} tem {} anos em {}'.format(nasc, idade, atual))
if idade == 18:
    print('Deve se alistar imediatamente')
elif idade < 18:
    saldo = 18 - idade
    print('Ainda faltam {} ano(s) para o alistamento'.format(saldo))
    ano = atual + saldo
    print('Seu alistamento será em {}'.format(ano))
else:
    saldo = idade - 18
    print('Já passou {} ano(s) que deveria ter se alistado'.format(saldo))
    ano = atual - saldo
    print('Seu alistamento foi em {}'.format(ano))
