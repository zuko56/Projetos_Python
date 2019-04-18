nome = str(input('Digite seu nome completo: ').strip())
div = nome.split()
print('Seu primeiro nome é {} e seu último nome é {}'.format(div[0], div[len(div)-1]))
