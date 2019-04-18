produto = float(input('Digite o valor do produto: '))
print('''Formas de pagamento 
(1) à vista dinheiro/cheque
(2) à vista cartão
(3) 2x no cartão
(4) 3x ou mais no cartão''')
opçao = int(input('Digite a forma de pagamento: '))
if opçao == 1:
    total = produto - (produto * 10/100)
    print('O valor com 10% de desconto será de R${:.2f}'.format(total))
elif opçao == 2:
    total = produto - (produto * 5/100)
    print('O valor com 5% de desconto será de R${:.2f}'.format(total))
elif opçao == 3:
    total = produto
    parcela = total / 2
    print('O valor pago 2x no cartão terá o valor das parcelas de R${:.2f} com o total de R${:.2f}'.format(parcela, total))
elif opçao == 4:
    total = produto + (produto * 20/100)
    totparc = int(input('Quantas parcelas? '))
    parcela = total / totparc
    print('Sua compra será parcelada em {}x de R${:.2f} com juros e no final irá custar {:.2f}'.format(totparc, parcela, total))
else:
    print('Opção inválida, tente novamente')





