t = int(input('Digite o valor da temperatura: '))
print('Essa temperatura em C para F é {} e em F para C é {:.2f}'.format(((t*9)/5)+32, ((t-32)*5)/9))