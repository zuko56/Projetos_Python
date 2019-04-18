soma = cont = menor = contmenor = 0
barato = ''
while True:
    nome = str(input('Digite o nome do produto: ')).strip().title()
    preco = float(input('Digite o preço do produto R$: '))
    if preco > 1000:
        cont += 1
    perg = str(input('Deseja continuar? [S/N]: ')).strip().upper()
    soma += preco
    contmenor += 1
    if contmenor == 1 or preco < menor:
        menor = preco
        barato = nome
    while perg not in 'SN':
        perg = str(input('Deseja continuar? [S/N]: ')).strip().upper()
    if perg == 'N':
        break
print(f'O total gasto na compra foi R${soma:.2f}')
print(f'{cont} produto(s) custam mais de 1k')
print(f'O produto mais barato foi {barato} e custa R${menor:.2f}')
