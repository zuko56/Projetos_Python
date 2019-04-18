perg = 'S'
cont = soma = media = 0
while perg == 'S':
    num = int(input('Digite um número: '))
    perg = str(input('Deseja continuar? [S/N]: ')).upper().strip()
    soma += num
    cont += 1
    if cont == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
media = soma / cont
print('Foram digitados {} números e a média é {:.2f}'.format(cont, media))
print('O maior valor digitado foi {} e o menor é {}'.format(maior, menor))
