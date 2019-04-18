sexo = str(input('Digite seu sexo [M/F]: ')).strip().upper()
while sexo not in 'MF':
    sexo = str(input('Digite M ou F: ')).strip().upper()
print('O sexo {} foi registrado'.format(sexo))
