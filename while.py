n = 1
contpar = contimpar = 0
while n != 0:
    n = int(input('Digite um numero: '))
    if n != 0:
        if n % 2 == 0:
            contpar += 1
        elif n % 2 != 0:
            contimpar += 1
print('O total de numeros pares foi {} e impares foi {}'.format(contpar, contimpar))
