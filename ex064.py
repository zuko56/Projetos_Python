n = soma = cont = 0
while n != 1:
    num = int(input('Digite um valor inteiro [999 para parar]: '))
    if num != 999:
        soma += num
        cont += 1
    else:
        break
print('O total de números digitados foi {} e a soma deles é {}'.format(cont, soma))

