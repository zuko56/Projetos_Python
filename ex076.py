tupla = ('Caneta', 0.50, 'Lápis', 0.20, 'Caderno', 20.00, 'Calculadora', 5, 'Mochila', 110.00, 'Estojo', 15.00, 'Livro', 35.00)
print('=' * 40)
print(f'{"TABELA DE PREÇOS":^40}')
print('=' * 40)
for pos in range(0, len(tupla)):
    if pos % 2 == 0:
        print(f'{tupla[pos]:.<30}', end='')
    else:
        print(f'R${tupla[pos]:>7.2f}')
print('=' * 40)
