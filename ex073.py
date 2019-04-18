tabela = ('Palmeiras', 'Flamengo', 'Internacional', 'Grêmio', 'São Paulo', 'Atlético-MG', 'Athletico-PR', 'Cruzeiro', 'Botafogo', 'Santos', 'Bahia', 'Fluminense', 'Corinthians', 'Chapecoense', 'Ceará', 'Vasco', 'Sport', 'América-MG', 'Vitória', 'Paraná')
print(f'Os primeiros cinco colocados são {tabela[0:5]}')
print('=' * 98)
print(f'Os últimos quatro colocados são {tabela[16:]}')
print('=' * 76)
print(f'Times em ordem alfabética {sorted(tabela)}')
print('=' * 272)
print(f'O Chapecoense está na posição {tabela.index("Chapecoense") + 1}')

