frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = '' #inverso = [::-1] iria funcionar sem usar o for
for letra in range(len(junto) - 1, -1, -1):
   inverso += junto[letra]
if inverso == junto:
    print('A frase digitada foi {}, seu inverso é {}, então é um palindromo'.format(junto, inverso))
else:
    print('Não é um palindromo')


